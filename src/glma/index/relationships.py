"""Relationship extraction from tree-sitter ASTs.

Extracts structural relationships (calls, imports/includes, inheritance) from
parsed ASTs and resolves them against chunks stored in the database.
"""

from pathlib import Path
from typing import Optional

from tree_sitter import Node

from glma.models import Chunk, Language, Relationship, RelType, Confidence
from glma.index.parser import PARSER_CONFIGS, get_root_node
from glma.index.resolver import (
    build_import_map, resolve_callee, find_enclosing_class,
    find_enclosing_function, ImportInfo,
)
from glma.db.ladybug_store import LadybugStore


def _find_enclosing_chunk(node: Node, chunks: list[Chunk]) -> Optional[Chunk]:
    """Walk up the node's parent chain to find the nearest enclosing chunk.

    Matches by start_line (1-indexed) to find the corresponding Chunk object.
    Returns None if no enclosing chunk found (module-level code).
    """
    current = node.parent
    while current is not None:
        start_line = current.start_point[0] + 1
        for chunk in chunks:
            if chunk.start_line == start_line:
                return chunk
        current = current.parent
    return None


def _extract_c_calls(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract C function call relationships from an AST."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "call_expression":
            callee = n.child_by_field_name("function")
            if callee is None and len(n.children) > 0:
                callee = n.children[0]

            if callee is not None and callee.type == "identifier":
                callee_name = callee.text.decode("utf-8")
                source_line = n.start_point[0] + 1

                enclosing = _find_enclosing_chunk(n, source_chunks)
                if enclosing is None:
                    _walk_children(n)
                    return

                target_chunk = None
                for chunk in source_chunks:
                    if chunk.name == callee_name:
                        target_chunk = chunk
                        break

                if target_chunk is not None:
                    relationships.append(Relationship(
                        source_id=enclosing.id,
                        target_id=target_chunk.id,
                        target_name=callee_name,
                        rel_type=RelType.CALLS,
                        confidence=Confidence.DIRECT,
                        source_line=source_line,
                    ))
                else:
                    relationships.append(Relationship(
                        source_id=enclosing.id,
                        target_id="",
                        target_name=callee_name,
                        rel_type=RelType.CALLS,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))

        _walk_children(n)

    def _walk_children(n: Node) -> None:
        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_c_includes(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
    indexed_files: dict[str, str],
) -> list[Relationship]:
    """Extract C #include relationships from an AST."""
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type == "preproc_include":
            source_line = n.start_point[0] + 1

            for child in n.children:
                if child.type == "string_literal":
                    content_child = child.child_by_field_name("content")
                    if content_child is None:
                        text = child.text.decode("utf-8")
                        include_path = text.strip('"')
                    else:
                        include_path = content_child.text.decode("utf-8")

                    resolved = False
                    for idx_path in indexed_files:
                        if idx_path.endswith(include_path):
                            relationships.append(Relationship(
                                source_id=source_id,
                                target_id="",
                                target_name=include_path,
                                rel_type=RelType.INCLUDES,
                                confidence=Confidence.DIRECT,
                                source_line=source_line,
                            ))
                            resolved = True
                            break

                    if not resolved:
                        relationships.append(Relationship(
                            source_id=source_id,
                            target_id="",
                            target_name=include_path,
                            rel_type=RelType.INCLUDES,
                            confidence=Confidence.INFERRED,
                            source_line=source_line,
                        ))

                elif child.type == "system_lib_string":
                    text = child.text.decode("utf-8")
                    include_name = text.strip("<>")
                    relationships.append(Relationship(
                        source_id=source_id,
                        target_id="",
                        target_name=include_name,
                        rel_type=RelType.INCLUDES,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def extract_c_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Extract all relationships from a C source file."""
    root = get_root_node(filepath, language)
    if root is None:
        return []

    indexed_files = store.get_indexed_files()

    calls = _extract_c_calls(root, source_chunks, str(filepath.relative_to(repo_root)))
    includes = _extract_c_includes(root, source_chunks, str(filepath.relative_to(repo_root)), indexed_files)

    return calls + includes


def _extract_cpp_using_declarations(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract C++ using declarations from an AST."""
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type == "using_declaration":
            source_line = n.start_point[0] + 1
            text = n.text.decode("utf-8").strip()
            name_part = text
            if name_part.startswith("using "):
                name_part = name_part[6:]
            if name_part.endswith(";"):
                name_part = name_part[:-1].strip()
            if name_part.startswith("namespace "):
                name_part = name_part[10:]

            if name_part:
                relationships.append(Relationship(
                    source_id=source_id,
                    target_id="",
                    target_name=name_part,
                    rel_type=RelType.IMPORTS,
                    confidence=Confidence.INFERRED,
                    source_line=source_line,
                ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_cpp_inheritance(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract C++ class inheritance from class_specifier nodes."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "class_specifier":
            name_node = n.child_by_field_name("name")
            if name_node is None:
                for child in n.children:
                    _walk(child)
                return

            class_name = name_node.text.decode("utf-8")
            class_chunk = None
            for chunk in source_chunks:
                if chunk.name == class_name and chunk.chunk_type.value == "class":
                    class_chunk = chunk
                    break

            if class_chunk is None:
                for child in n.children:
                    _walk(child)
                return

            for child in n.children:
                if child.type == "base_class_clause":
                    for base_child in child.children:
                        if base_child.type == "type_identifier":
                            base_name = base_child.text.decode("utf-8")
                            target_chunk = None
                            for chunk in source_chunks:
                                if chunk.name == base_name:
                                    target_chunk = chunk
                                    break

                            if target_chunk is not None:
                                relationships.append(Relationship(
                                    source_id=class_chunk.id,
                                    target_id=target_chunk.id,
                                    target_name=base_name,
                                    rel_type=RelType.INHERITS,
                                    confidence=Confidence.DIRECT,
                                    source_line=n.start_point[0] + 1,
                                ))
                            else:
                                relationships.append(Relationship(
                                    source_id=class_chunk.id,
                                    target_id="",
                                    target_name=base_name,
                                    rel_type=RelType.INHERITS,
                                    confidence=Confidence.INFERRED,
                                    source_line=n.start_point[0] + 1,
                                ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def extract_cpp_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Extract all relationships from a C++ source file."""
    root = get_root_node(filepath, language)
    if root is None:
        return []

    relative_path = str(filepath.relative_to(repo_root))
    indexed_files = store.get_indexed_files()

    calls = _extract_c_calls(root, source_chunks, relative_path)
    includes = _extract_c_includes(root, source_chunks, relative_path, indexed_files)
    using = _extract_cpp_using_declarations(root, source_chunks, relative_path)
    inheritance = _extract_cpp_inheritance(root, source_chunks, relative_path)

    return calls + includes + using + inheritance


def _extract_python_calls(
    node: Node,
    source_chunks: list[Chunk],
    import_map: dict[str, ImportInfo],
    store: LadybugStore,
    file_path: str,
) -> list[Relationship]:
    """Extract Python function call relationships from an AST."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "call":
            source_line = n.start_point[0] + 1
            callee = n.children[0] if n.children else None

            if callee is not None:
                enclosing_id = find_enclosing_function(n, source_chunks)
                if enclosing_id is None:
                    for child in n.children:
                        _walk(child)
                    return

                enclosing_class = find_enclosing_class(n)

                target_id, target_name = resolve_callee(
                    callee, import_map, enclosing_class, store, file_path, source_chunks
                )

                if target_id:
                    confidence = Confidence.DIRECT
                elif (callee.type == "attribute"
                      and callee.child_by_field_name("object") is not None
                      and callee.child_by_field_name("object").text.decode("utf-8") == "self"):
                    confidence = Confidence.INFERRED
                else:
                    confidence = Confidence.INFERRED

                relationships.append(Relationship(
                    source_id=enclosing_id,
                    target_id=target_id,
                    target_name=target_name,
                    rel_type=RelType.CALLS,
                    confidence=confidence,
                    source_line=source_line,
                ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_python_imports(
    node: Node,
    source_chunks: list[Chunk],
    import_map: dict[str, ImportInfo],
    store: LadybugStore,
    file_path: str,
) -> list[Relationship]:
    """Extract Python import relationships."""
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type in ("import_statement", "import_from_statement"):
            source_line = n.start_point[0] + 1
            local_imports = build_import_map(n)

            for local_name, info in local_imports.items():
                module_path = info.source_module.replace(".", "/")
                possible_paths = [
                    f"{module_path}.py",
                    f"{module_path}/__init__.py",
                ]

                resolved = False
                for try_path in possible_paths:
                    try:
                        result = store.conn.execute(
                            "MATCH (f:File {path: $fp}) RETURN f.path LIMIT 1",
                            {"fp": try_path},
                        )
                        rows = list(result)
                        if rows:
                            relationships.append(Relationship(
                                source_id=source_id,
                                target_id="",
                                target_name=try_path,
                                rel_type=RelType.IMPORTS,
                                confidence=Confidence.DIRECT,
                                source_line=source_line,
                            ))
                            resolved = True
                            break
                    except Exception:
                        pass

                if not resolved:
                    relationships.append(Relationship(
                        source_id=source_id,
                        target_id="",
                        target_name=info.source_module,
                        rel_type=RelType.IMPORTS,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_python_inheritance(
    node: Node,
    source_chunks: list[Chunk],
    store: LadybugStore,
    file_path: str,
) -> list[Relationship]:
    """Extract Python class inheritance relationships."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "class_definition":
            class_name_node = n.child_by_field_name("name")
            if class_name_node is None:
                for child in n.children:
                    _walk(child)
                return

            class_name = class_name_node.text.decode("utf-8")
            class_chunk = None
            for chunk in source_chunks:
                if chunk.name == class_name and chunk.chunk_type.value == "class":
                    class_chunk = chunk
                    break

            if class_chunk is None:
                for child in n.children:
                    _walk(child)
                return

            for child in n.children:
                if child.type == "argument_list":
                    for arg in child.children:
                        if arg.type == "identifier":
                            base_name = arg.text.decode("utf-8")

                            # Check same-file chunks
                            target_chunk = None
                            for chunk in source_chunks:
                                if chunk.name == base_name:
                                    target_chunk = chunk
                                    break

                            if target_chunk is not None:
                                relationships.append(Relationship(
                                    source_id=class_chunk.id,
                                    target_id=target_chunk.id,
                                    target_name=base_name,
                                    rel_type=RelType.INHERITS,
                                    confidence=Confidence.DIRECT,
                                    source_line=n.start_point[0] + 1,
                                ))
                            else:
                                # Check store for cross-file
                                found = False
                                try:
                                    result = store.conn.execute(
                                        "MATCH (c:Chunk {name: $name}) RETURN c.id LIMIT 1",
                                        {"name": base_name},
                                    )
                                    rows = list(result)
                                    if rows:
                                        relationships.append(Relationship(
                                            source_id=class_chunk.id,
                                            target_id=rows[0][0],
                                            target_name=base_name,
                                            rel_type=RelType.INHERITS,
                                            confidence=Confidence.DIRECT,
                                            source_line=n.start_point[0] + 1,
                                        ))
                                        found = True
                                except Exception:
                                    pass

                                if not found:
                                    relationships.append(Relationship(
                                        source_id=class_chunk.id,
                                        target_id="",
                                        target_name=base_name,
                                        rel_type=RelType.INHERITS,
                                        confidence=Confidence.INFERRED,
                                        source_line=n.start_point[0] + 1,
                                    ))

                        elif arg.type == "attribute":
                            base_name = arg.text.decode("utf-8")
                            relationships.append(Relationship(
                                source_id=class_chunk.id,
                                target_id="",
                                target_name=base_name,
                                rel_type=RelType.INHERITS,
                                confidence=Confidence.INFERRED,
                                source_line=n.start_point[0] + 1,
                            ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def extract_python_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Extract all relationships from a Python source file."""
    root = get_root_node(filepath, language)
    if root is None:
        return []

    relative_path = str(filepath.relative_to(repo_root))
    import_map = build_import_map(root)

    calls = _extract_python_calls(root, source_chunks, import_map, store, relative_path)
    imports = _extract_python_imports(root, source_chunks, import_map, store, relative_path)
    inheritance = _extract_python_inheritance(root, source_chunks, store, relative_path)

    return calls + imports + inheritance


def _extract_ts_imports(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract TypeScript import relationships."""
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type == "import_statement":
            source_line = n.start_point[0] + 1
            for child in n.children:
                if child.type in ("string_literal", "string"):
                    text = child.text.decode("utf-8")
                    # Strip quotes
                    content = text.strip("'\"")
                    relationships.append(Relationship(
                        source_id=source_id,
                        target_id="",
                        target_name=content,
                        rel_type=RelType.IMPORTS,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_ts_calls(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract TypeScript function/method call relationships."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "call_expression":
            callee = n.children[0] if n.children else None
            if callee is None:
                for child in n.children:
                    _walk(child)
                return

            source_line = n.start_point[0] + 1
            enclosing = _find_enclosing_chunk(n, source_chunks)
            if enclosing is None:
                for child in n.children:
                    _walk(child)
                return

            callee_name = callee.text.decode("utf-8")
            simple_name = callee_name.split(".")[-1]

            target_chunk = None
            for chunk in source_chunks:
                if chunk.name == simple_name:
                    target_chunk = chunk
                    break

            if target_chunk is not None:
                relationships.append(Relationship(
                    source_id=enclosing.id,
                    target_id=target_chunk.id,
                    target_name=callee_name,
                    rel_type=RelType.CALLS,
                    confidence=Confidence.DIRECT,
                    source_line=source_line,
                ))
            else:
                relationships.append(Relationship(
                    source_id=enclosing.id,
                    target_id="",
                    target_name=callee_name,
                    rel_type=RelType.CALLS,
                    confidence=Confidence.INFERRED,
                    source_line=source_line,
                ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_ts_heritage(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract TypeScript extends and implements relationships."""
    relationships: list[Relationship] = []

    def _get_class_name(n: Node) -> Optional[str]:
        name_node = n.child_by_field_name("name")
        if name_node:
            return name_node.text.decode("utf-8")
        # Fallback: find type_identifier child
        for child in n.children:
            if child.type == "type_identifier":
                return child.text.decode("utf-8")
        return None

    def _walk(n: Node) -> None:
        if n.type == "class_declaration":
            class_name = _get_class_name(n)
            if class_name is None:
                for child in n.children:
                    _walk(child)
                return

            class_chunk = None
            for chunk in source_chunks:
                if chunk.name == class_name and chunk.chunk_type.value == "class":
                    class_chunk = chunk
                    break

            if class_chunk is None:
                for child in n.children:
                    _walk(child)
                return

            for child in n.children:
                if child.type == "class_heritage":
                    for heritage_child in child.children:
                        if heritage_child.type == "extends_clause":
                            for ext in heritage_child.children:
                                if ext.type in ("type_identifier", "identifier"):
                                    base_name = ext.text.decode("utf-8")
                                    target_chunk = None
                                    for chunk in source_chunks:
                                        if chunk.name == base_name:
                                            target_chunk = chunk
                                            break
                                    rels_target_id = target_chunk.id if target_chunk else ""
                                    confidence = Confidence.DIRECT if target_chunk else Confidence.INFERRED
                                    relationships.append(Relationship(
                                        source_id=class_chunk.id,
                                        target_id=rels_target_id,
                                        target_name=base_name,
                                        rel_type=RelType.INHERITS,
                                        confidence=confidence,
                                        source_line=n.start_point[0] + 1,
                                    ))
                        elif heritage_child.type == "implements_clause":
                            for impl in heritage_child.children:
                                if impl.type in ("type_identifier", "identifier"):
                                    iface_name = impl.text.decode("utf-8")
                                    target_chunk = None
                                    for chunk in source_chunks:
                                        if chunk.name == iface_name:
                                            target_chunk = chunk
                                            break
                                    rels_target_id = target_chunk.id if target_chunk else ""
                                    confidence = Confidence.DIRECT if target_chunk else Confidence.INFERRED
                                    relationships.append(Relationship(
                                        source_id=class_chunk.id,
                                        target_id=rels_target_id,
                                        target_name=iface_name,
                                        rel_type=RelType.IMPLEMENTS,
                                        confidence=confidence,
                                        source_line=n.start_point[0] + 1,
                                    ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def extract_typescript_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Extract all relationships from a TypeScript/TSX source file."""
    root = get_root_node(filepath, language)
    if root is None:
        return []

    relative_path = str(filepath.relative_to(repo_root))
    imports = _extract_ts_imports(root, source_chunks, relative_path)
    calls = _extract_ts_calls(root, source_chunks, relative_path)
    heritage = _extract_ts_heritage(root, source_chunks, relative_path)

    return imports + calls + heritage


def _extract_rust_use(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract Rust use declarations as import relationships."""
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type == "use_declaration":
            source_line = n.start_point[0] + 1
            for child in n.children:
                if child.type in ("scoped_identifier", "scoped_use_list", "use_list", "identifier"):
                    use_path = child.text.decode("utf-8").strip()
                    relationships.append(Relationship(
                        source_id=source_id,
                        target_id="",
                        target_name=use_path,
                        rel_type=RelType.IMPORTS,
                        confidence=Confidence.INFERRED,
                        source_line=source_line,
                    ))
                    break
            else:
                text = n.text.decode("utf-8").strip()
                if text.startswith("use "):
                    path = text[4:].rstrip(";").strip()
                    if path:
                        relationships.append(Relationship(
                            source_id=source_id,
                            target_id="",
                            target_name=path,
                            rel_type=RelType.IMPORTS,
                            confidence=Confidence.INFERRED,
                            source_line=source_line,
                        ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_rust_calls(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract Rust function call relationships."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "call_expression":
            callee = n.children[0] if n.children else None
            if callee is None:
                for child in n.children:
                    _walk(child)
                return

            source_line = n.start_point[0] + 1
            enclosing = _find_enclosing_chunk(n, source_chunks)
            if enclosing is None:
                for child in n.children:
                    _walk(child)
                return

            callee_name = callee.text.decode("utf-8")
            simple_name = callee_name.split("::")[-1]
            if "." in simple_name:
                simple_name = simple_name.split(".")[-1]

            target_chunk = None
            for chunk in source_chunks:
                if chunk.name == simple_name:
                    target_chunk = chunk
                    break

            if target_chunk is not None:
                relationships.append(Relationship(
                    source_id=enclosing.id,
                    target_id=target_chunk.id,
                    target_name=callee_name,
                    rel_type=RelType.CALLS,
                    confidence=Confidence.DIRECT,
                    source_line=source_line,
                ))
            else:
                relationships.append(Relationship(
                    source_id=enclosing.id,
                    target_id="",
                    target_name=callee_name,
                    rel_type=RelType.CALLS,
                    confidence=Confidence.INFERRED,
                    source_line=source_line,
                ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_rust_impl(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract Rust impl relationships (impl Trait for Type)."""
    relationships: list[Relationship] = []

    def _walk(n: Node) -> None:
        if n.type == "impl_item":
            children = n.children
            trait_name = None
            impl_type = None
            has_for = False

            for i, child in enumerate(children):
                if child.type == "for":
                    has_for = True
                    if i > 0 and children[i-1].type in ("type_identifier", "identifier"):
                        trait_name = children[i-1].text.decode("utf-8")
                    if i + 1 < len(children) and children[i+1].type in ("type_identifier", "identifier"):
                        impl_type = children[i+1].text.decode("utf-8")

            if trait_name and impl_type:
                type_chunk = None
                for chunk in source_chunks:
                    if chunk.name == impl_type and chunk.chunk_type.value == "class":
                        type_chunk = chunk
                        break

                if type_chunk is not None:
                    relationships.append(Relationship(
                        source_id=type_chunk.id,
                        target_id="",
                        target_name=trait_name,
                        rel_type=RelType.INHERITS,
                        confidence=Confidence.INFERRED,
                        source_line=n.start_point[0] + 1,
                    ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def _extract_rust_mod(
    node: Node,
    source_chunks: list[Chunk],
    file_path: str,
) -> list[Relationship]:
    """Extract Rust mod declarations as module reference relationships."""
    relationships: list[Relationship] = []
    source_id = source_chunks[0].id if source_chunks else ""

    def _walk(n: Node) -> None:
        if n.type == "mod_item":
            source_line = n.start_point[0] + 1
            name_node = n.child_by_field_name("name")
            if name_node:
                mod_name = name_node.text.decode("utf-8")
                relationships.append(Relationship(
                    source_id=source_id,
                    target_id="",
                    target_name=mod_name,
                    rel_type=RelType.INCLUDES,
                    confidence=Confidence.INFERRED,
                    source_line=source_line,
                ))

        for child in n.children:
            _walk(child)

    _walk(node)
    return relationships


def extract_rust_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Extract all relationships from a Rust source file."""
    root = get_root_node(filepath, language)
    if root is None:
        return []

    relative_path = str(filepath.relative_to(repo_root))
    use_rels = _extract_rust_use(root, source_chunks, relative_path)
    calls = _extract_rust_calls(root, source_chunks, relative_path)
    impl_rels = _extract_rust_impl(root, source_chunks, relative_path)
    mod_rels = _extract_rust_mod(root, source_chunks, relative_path)

    return use_rels + calls + impl_rels + mod_rels


def extract_relationships(
    filepath: Path,
    language: Language,
    repo_root: Path,
    source_chunks: list[Chunk],
    store: LadybugStore,
) -> list[Relationship]:
    """Dispatcher: extract relationships based on language."""
    if language == Language.C:
        return extract_c_relationships(filepath, language, repo_root, source_chunks, store)
    elif language == Language.CPP:
        return extract_cpp_relationships(filepath, language, repo_root, source_chunks, store)
    elif language == Language.PYTHON:
        return extract_python_relationships(filepath, language, repo_root, source_chunks, store)
    elif language in (Language.TYPESCRIPT, Language.TSX):
        return extract_typescript_relationships(filepath, language, repo_root, source_chunks, store)
    elif language == Language.RUST:
        return extract_rust_relationships(filepath, language, repo_root, source_chunks, store)

    return []
