"""Per-statement variable extraction for Jupyter notebook cells.

Uses Python's ast module to track which names each statement defines and references,
enabling cross-cell variable flow analysis.
"""

import ast
from dataclasses import dataclass, field


@dataclass
class StatementInfo:
    """Variable info for a single statement within a cell."""
    line_number: int          # 1-indexed line within the cell
    statement_type: str       # "assign", "function_def", "class_def", "import", etc.
    defines: list[str]        # Names defined by this statement
    references: list[str]     # Names referenced by this statement


@dataclass
class CellVariableInfo:
    """Variable info for a single notebook cell."""
    cell_index: int           # 0-indexed cell number
    cell_type: str            # "code" or "markdown"
    source: str               # Raw cell source
    statements: list[StatementInfo] = field(default_factory=list)
    all_defines: list[str] = field(default_factory=list)
    all_references: list[str] = field(default_factory=list)


def _extract_name_refs(node: ast.AST) -> list[str]:
    """Extract all Name references (Load context) from an AST subtree.

    Skips nested function/class definitions to avoid counting inner-scope names.
    """
    # Check if the node itself is a Name reference
    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
        return [node.id]
    names: list[str] = []
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue  # Don't descend into nested scopes
        else:
            names.extend(_extract_name_refs(child))
    return names


def _extract_definition_names(node: ast.AST) -> list[str]:
    """Extract names from an assignment target (Name, Tuple, List)."""
    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
        return [node.id]
    elif isinstance(node, (ast.Tuple, ast.List)):
        names: list[str] = []
        for elt in node.elts:
            names.extend(_extract_definition_names(elt))
        return names
    elif isinstance(node, ast.Starred):
        return _extract_definition_names(node.value)
    return []


def extract_cell_variables(cell_source: str, cell_index: int) -> CellVariableInfo:
    """Extract variable definitions and references for each statement in a cell.

    Args:
        cell_source: The cell's source code.
        cell_index: 0-indexed cell number.

    Returns:
        CellVariableInfo with per-statement analysis.
    """
    try:
        tree = ast.parse(cell_source)
    except SyntaxError:
        return CellVariableInfo(
            cell_index=cell_index,
            cell_type="code",
            source=cell_source,
        )

    statements: list[StatementInfo] = []

    for node in tree.body:
        defines: list[str] = []
        references: list[str] = []
        stmt_type = "other"

        if isinstance(node, ast.Assign):
            stmt_type = "assign"
            for target in node.targets:
                defines.extend(_extract_definition_names(target))
            references = _extract_name_refs(node.value)

        elif isinstance(node, ast.AugAssign):
            stmt_type = "aug_assign"
            defines = _extract_definition_names(node.target)
            # Aug assign reads the variable too
            references = _extract_name_refs(node.value) + defines

        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            stmt_type = "function_def"
            defines = [node.name]
            # References: arg names, defaults, decorators, annotations
            refs: list[str] = []
            for arg in node.args.args + node.args.posonlyargs + node.args.kwonlyargs:
                refs.append(arg.arg)
                if arg.annotation:
                    refs.extend(_extract_name_refs(arg.annotation))
            if node.args.vararg:
                refs.append(node.args.vararg.arg)
            if node.args.kwarg:
                refs.append(node.args.kwarg.arg)
            for default in node.args.defaults + node.args.kw_defaults:
                if default:
                    refs.extend(_extract_name_refs(default))
            for decorator in node.decorator_list:
                refs.extend(_extract_name_refs(decorator))
            if node.returns:
                refs.extend(_extract_name_refs(node.returns))
            references = refs

        elif isinstance(node, ast.ClassDef):
            stmt_type = "class_def"
            defines = [node.name]
            references = []
            for base in node.bases:
                references.extend(_extract_name_refs(base))
            for decorator in node.decorator_list:
                references.extend(_extract_name_refs(decorator))
            for kw in node.keywords:
                references.extend(_extract_name_refs(kw.value))

        elif isinstance(node, ast.Import):
            stmt_type = "import"
            for alias in node.names:
                defines.append(alias.asname or alias.name.split(".")[0])

        elif isinstance(node, ast.ImportFrom):
            stmt_type = "import"
            for alias in node.names:
                defines.append(alias.asname or alias.name)

        elif isinstance(node, (ast.For, ast.AsyncFor)):
            stmt_type = "for_loop"
            defines = _extract_definition_names(node.target)
            references = _extract_name_refs(node.iter)

        elif isinstance(node, (ast.With, ast.AsyncWith)):
            stmt_type = "with_stmt"
            for item in node.items:
                references.extend(_extract_name_refs(item.context_expr))
                if item.optional_vars:
                    defines.extend(_extract_definition_names(item.optional_vars))

        elif isinstance(node, ast.Return):
            stmt_type = "return"
            if node.value:
                references = _extract_name_refs(node.value)

        elif isinstance(node, ast.Expr):
            stmt_type = "expr"
            references = _extract_name_refs(node.value)

        statements.append(StatementInfo(
            line_number=node.lineno,
            statement_type=stmt_type,
            defines=defines,
            references=references,
        ))

    # Aggregate all defines and references (deduplicated, order-preserved)
    all_defines: list[str] = []
    all_references: list[str] = []
    seen_def = set()
    seen_ref = set()
    for stmt in statements:
        for name in stmt.defines:
            if name not in seen_def:
                all_defines.append(name)
                seen_def.add(name)
        for name in stmt.references:
            if name not in seen_ref:
                all_references.append(name)
                seen_ref.add(name)

    return CellVariableInfo(
        cell_index=cell_index,
        cell_type="code",
        source=cell_source,
        statements=statements,
        all_defines=all_defines,
        all_references=all_references,
    )


def build_variable_flow(cells: list[CellVariableInfo]) -> dict[str, dict]:
    """Build cross-cell variable flow map.

    Args:
        cells: List of CellVariableInfo objects from all cells.

    Returns:
        Dict mapping variable name to {"defined_in": [...], "used_in": [...]}.
        Each entry is {"cell": int, "line": int}.
    """
    defined_vars: dict[str, list[dict]] = {}
    used_vars: dict[str, list[dict]] = {}

    # First pass: collect all definitions
    for cell in cells:
        for stmt in cell.statements:
            for name in stmt.defines:
                if name not in defined_vars:
                    defined_vars[name] = []
                defined_vars[name].append({"cell": cell.cell_index, "line": stmt.line_number})

    # Second pass: collect usages that reference defined variables
    for cell in cells:
        for stmt in cell.statements:
            for name in stmt.references:
                if name in defined_vars:
                    if name not in used_vars:
                        used_vars[name] = []
                    # Only add usage if it's in a different statement or cell than definition
                    used_vars[name].append({"cell": cell.cell_index, "line": stmt.line_number})

    # Merge into result
    result: dict[str, dict] = {}
    all_vars = set(defined_vars.keys()) | set(used_vars.keys())
    for var in all_vars:
        result[var] = {
            "defined_in": defined_vars.get(var, []),
            "used_in": used_vars.get(var, []),
        }

    return result
