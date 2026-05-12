"""Cross-file resolution for Python relationships.

Builds per-file import maps and resolves callee names to target chunks
using the LadybugStore database.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from tree_sitter import Node

from glma.models import Language
from glma.db.ladybug_store import LadybugStore


@dataclass
class ImportInfo:
    """Information about a single import."""
    local_name: str  # Name used in the importing file (alias or imported name)
    source_module: str  # Dotted module path (e.g., "pathlib", "foo.bar")
    imported_name: Optional[str]  # Specific name imported (e.g., "Path"), None for module-level


def build_import_map(node: Node) -> dict[str, ImportInfo]:
    """Build a map of local names to import information from an AST.

    Handles:
    - `import os` → {"os": ImportInfo("os", "os", None)}
    - `import foo.bar as baz` → {"baz": ImportInfo("baz", "foo.bar", None)}
    - `import foo.bar` → {"foo": ImportInfo("foo", "foo.bar", None)}
    - `from pathlib import Path` → {"Path": ImportInfo("Path", "pathlib", "Path")}
    - `from typing import Optional, List` → multiple entries

    Args:
        node: Root AST node to walk.

    Returns:
        Dict mapping local_name → ImportInfo.
    """
    import_map: dict[str, ImportInfo] = {}

    def _walk(n: Node) -> None:
        if n.type == "import_statement":
            _handle_import_statement(n)
        elif n.type == "import_from_statement":
            _handle_import_from_statement(n)

        for child in n.children:
            _walk(child)

    def _handle_import_statement(n: Node) -> None:
        """Handle `import X` and `import X as Y` statements."""
        for child in n.children:
            if child.type == "aliased_import":
                # import foo.bar as baz
                dotted_name_node = child.child_by_field_name("name")
                alias_node = child.child_by_field_name("alias")

                if dotted_name_node and alias_node:
                    module_path = dotted_name_node.text.decode("utf-8")
                    alias = alias_node.text.decode("utf-8")
                    import_map[alias] = ImportInfo(
                        local_name=alias,
                        source_module=module_path,
                        imported_name=None,
                    )
            elif child.type == "dotted_name":
                # import foo.bar (no alias)
                module_path = child.text.decode("utf-8")
                # Use first component as local_name
                first_component = module_path.split(".")[0]
                import_map[first_component] = ImportInfo(
                    local_name=first_component,
                    source_module=module_path,
                    imported_name=None,
                )

    def _handle_import_from_statement(n: Node) -> None:
        """Handle `from X import Y` and `from X import Y as Z` statements."""
        children = n.children
        module_path = ""
        imported_names: list[tuple[str, str]] = []  # (name, alias)

        # Structure: from <dotted_name> import <name> [, <name>]* [, <aliased_import>]*
        # Or: from <dotted_name> import (<name> ...)
        state = "start"
        for child in children:
            if child.type == "dotted_name" and state == "start":
                # The first dotted_name after 'from' is the module
                if not module_path:
                    module_path = child.text.decode("utf-8")
                    state = "after_module"
            elif child.type == "aliased_import" and state in ("after_import", "after_module"):
                # from X import Y as Z
                name_node = child.child_by_field_name("name")
                alias_node = child.child_by_field_name("alias")
                if name_node and alias_node:
                    name = name_node.text.decode("utf-8")
                    alias = alias_node.text.decode("utf-8")
                    imported_names.append((alias, name))
            elif child.type == "identifier" and state == "after_import":
                imported_names.append((child.text.decode("utf-8"), child.text.decode("utf-8")))
            elif child.type == "dotted_name" and state == "after_import":
                # from X import Y.Z  (rare but valid)
                name = child.text.decode("utf-8")
                imported_names.append((name, name))
            elif child.type == "wildcard_import":
                # from X import * — skip, can't resolve individual names
                pass

            if child.type == "import":
                state = "after_import"

        # Also handle parenthesized imports: from X import (Y, Z)
        # tree-sitter handles these as regular children after 'import'

        for local_name, orig_name in imported_names:
            import_map[local_name] = ImportInfo(
                local_name=local_name,
                source_module=module_path,
                imported_name=orig_name,
            )

    _walk(node)
    return import_map


def find_enclosing_class(node: Node) -> Optional[str]:
    """Walk up the parent chain to find the enclosing class name.

    Args:
        node: Starting AST node.

    Returns:
        Class name string, or None if at module level.
    """
    current = node.parent
    while current is not None:
        if current.type == "class_definition":
            # First identifier child is the class name
            for child in current.children:
                if child.type == "identifier":
                    return child.text.decode("utf-8")
        current = current.parent
    return None


def find_enclosing_function(node: Node, chunks: list) -> Optional[str]:
    """Walk up parent chain to find the enclosing function chunk ID.

    Args:
        node: Starting AST node.
        chunks: List of Chunk objects for the current file.

    Returns:
        Chunk ID of the enclosing function, or None.
    """
    current = node.parent
    while current is not None:
        if current.type == "function_definition":
            start_line = current.start_point[0] + 1
            for chunk in chunks:
                if chunk.start_line == start_line and chunk.chunk_type.value in ("function", "method"):
                    return chunk.id
        current = current.parent
    return None


def resolve_callee(
    callee_node: Node,
    import_map: dict[str, ImportInfo],
    enclosing_class: Optional[str],
    store: LadybugStore,
    file_path: str,
    source_chunks: list,
) -> tuple[str, str]:
    """Resolve a callee node to a target chunk ID and display name.

    Args:
        callee_node: The callee AST node from a call expression.
        import_map: Per-file import map.
        enclosing_class: Name of enclosing class, or None.
        store: LadybugStore for querying chunks.
        file_path: Current file's relative path.
        source_chunks: Chunks from the current file.

    Returns:
        (target_id, target_name) — target_id is "" if unresolved.
    """
    if callee_node.type == "identifier":
        callee_name = callee_node.text.decode("utf-8")

        # Check import map first
        if callee_name in import_map:
            import_info = import_map[callee_name]
            # Try to resolve to a file in the store
            module_path = import_info.source_module.replace(".", "/")
            if import_info.imported_name:
                # from X import Y — look for chunk named Y in the module file
                return _resolve_imported_name(import_info, store)
            else:
                # import X — look for chunks in the module file
                return _resolve_module(import_info.source_module, store)

        # Check same-file chunks
        for chunk in source_chunks:
            if chunk.name == callee_name:
                return (chunk.id, callee_name)

        # Unresolved
        return ("", callee_name)

    elif callee_node.type == "attribute":
        # e.g., self.method() or os.path.join() or obj.method()
        obj_node = callee_node.child_by_field_name("object")
        attr_node = callee_node.child_by_field_name("attribute")

        if obj_node is None or attr_node is None:
            return ("", callee_node.text.decode("utf-8"))

        obj_name = obj_node.text.decode("utf-8")
        attr_name = attr_node.text.decode("utf-8")
        full_name = f"{obj_name}.{attr_name}"

        # Case 1: self.method()
        if obj_name == "self" and enclosing_class is not None:
            # Look for method in the same class
            for chunk in source_chunks:
                if (chunk.name == attr_name
                    and chunk.parent_id is not None
                    and enclosing_class in chunk.parent_id):
                    return (chunk.id, full_name)

            # Also try: find method in same file with name matching and parent containing class name
            for chunk in source_chunks:
                if (chunk.name == attr_name
                    and chunk.parent_id is not None):
                    # Check if the parent_id contains the class name
                    parent_parts = chunk.parent_id.split("::")
                    if len(parent_parts) >= 3 and parent_parts[2] == enclosing_class:
                        return (chunk.id, full_name)

            return ("", full_name)

        # Case 2: object matches import map (e.g., os.path.join())
        if obj_name in import_map:
            import_info = import_map[obj_name]
            return _resolve_module(import_info.source_module, store, attr_name)

        # Case 3: Unknown object
        return ("", full_name)

    else:
        # Unexpected callee type
        return ("", callee_node.text.decode("utf-8"))


def _resolve_imported_name(import_info: ImportInfo, store: LadybugStore) -> tuple[str, str]:
    """Resolve a `from X import Y` import to a target chunk."""
    module_path = import_info.source_module.replace(".", "/")
    # Try with .py extension
    possible_paths = [
        f"{module_path}.py",
        f"{module_path}/__init__.py",
    ]

    for try_path in possible_paths:
        try:
            result = store.conn.execute(
                "MATCH (c:Chunk {name: $name, file_path: $fp}) RETURN c.id LIMIT 1",
                {"name": import_info.imported_name, "fp": try_path},
            )
            rows = list(result)
            if rows:
                return (rows[0][0], import_info.imported_name)
        except Exception:
            pass

    # Not found in store
    return ("", import_info.imported_name)


def _resolve_module(module: str, store: LadybugStore, attr_name: Optional[str] = None) -> tuple[str, str]:
    """Resolve a module import to a target chunk."""
    module_path = module.replace(".", "/")
    possible_paths = [
        f"{module_path}.py",
        f"{module_path}/__init__.py",
    ]

    if attr_name:
        for try_path in possible_paths:
            try:
                result = store.conn.execute(
                    "MATCH (c:Chunk {name: $name, file_path: $fp}) RETURN c.id LIMIT 1",
                    {"name": attr_name, "fp": try_path},
                )
                rows = list(result)
                if rows:
                    return (rows[0][0], attr_name)
            except Exception:
                pass
        return ("", attr_name)
    else:
        for try_path in possible_paths:
            try:
                result = store.conn.execute(
                    "MATCH (c:Chunk {file_path: $fp}) RETURN c.id LIMIT 1",
                    {"fp": try_path},
                )
                rows = list(result)
                if rows:
                    return (rows[0][0], module)
            except Exception:
                pass
        return ("", module)
