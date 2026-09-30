"""
parser.py
---------

Reads Python source code from a file and converts it into AST.

This module only handles reading and parsing.
It does not count stats.
"""

from pathlib import Path
import ast


def read_source(file_path: str) -> str:
    """Read Python source code from a file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix != ".py":
        raise ValueError("Only .py files are supported.")

    return path.read_text(encoding="utf-8")


def parse_source(source: str) -> ast.AST:
    """Convert Python source code into an AST tree."""
    return ast.parse(source)


def parse_file(file_path: str) -> ast.AST:
    """Read a file and return its AST tree."""
    source = read_source(file_path)
    return parse_source(source)