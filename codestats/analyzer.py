"""
analyzer.py
-----------

Analyzes Python source code and counts basic code statistics.

Supported v1.0 metrics:
- total lines
- blank lines
- comment lines
- code lines
- variables
- functions
- classes
- imports
- if / elif / else
- for loops
- while loops
- return statements
"""

import ast

from .models import CodeStats
from .parser import read_source, parse_source
from .utils import (
    count_total_lines,
    count_blank_lines,
    count_comment_lines,
)


class StatsVisitor(ast.NodeVisitor):
    """
    Walks through AST nodes and counts supported code structures.
    """

    def __init__(self) -> None:
        self.stats = CodeStats()

    def visit_Assign(self, node: ast.Assign) -> None:
        self.stats.variables += 1
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self.stats.variables += 1
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self.stats.variables += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.stats.functions += 1
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.stats.functions += 1
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.stats.classes += 1
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        self.stats.imports += 1
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        self.stats.imports += 1
        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:
        self.stats.for_loops += 1
        self.generic_visit(node)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        self.stats.for_loops += 1
        self.generic_visit(node)

    def visit_While(self, node: ast.While) -> None:
        self.stats.while_loops += 1
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        self.stats.returns += 1
        self.generic_visit(node)

    def visit_If(self, node: ast.If) -> None:
        self.stats.ifs += 1

        # Count "elif" by checking whether the orelse contains a single If node.
        if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            self.stats.elifs += 1
            self.visit(node.orelse[0])
        elif node.orelse:
            self.stats.elses += 1
            for child in node.orelse:
                self.visit(child)

        for child in node.body:
            self.visit(child)


def analyze(file_path: str) -> CodeStats:
    """
    Analyze a Python file and return all collected statistics.

    Parameters
    ----------
    file_path : str
        Path to the Python file.

    Returns
    -------
    CodeStats
        Object containing all code metrics.
    """
    source = read_source(file_path)

    stats = CodeStats()
    stats.total_lines = count_total_lines(source)
    stats.blank_lines = count_blank_lines(source)
    stats.comment_lines = count_comment_lines(source)
    stats.code_lines = stats.total_lines - stats.blank_lines

    tree = parse_source(source)

    visitor = StatsVisitor()
    visitor.visit(tree)

    # Copy AST-based counts into final stats object.
    stats.variables = visitor.stats.variables
    stats.functions = visitor.stats.functions
    stats.classes = visitor.stats.classes
    stats.imports = visitor.stats.imports
    stats.ifs = visitor.stats.ifs
    stats.elifs = visitor.stats.elifs
    stats.elses = visitor.stats.elses
    stats.for_loops = visitor.stats.for_loops
    stats.while_loops = visitor.stats.while_loops
    stats.returns = visitor.stats.returns

    return stats