"""
utils.py
--------

Small helper functions used across PyCodeStats.
"""

from pathlib import Path


def is_python_file(file_path: str) -> bool:
    """Return True if the file has a .py extension."""
    return Path(file_path).suffix.lower() == ".py"


def read_text(file_path: str) -> str:
    """Read and return file content as UTF-8 text."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Not a file: {file_path}")

    return path.read_text(encoding="utf-8")


def count_total_lines(text: str) -> int:
    """Count total lines in the given text."""
    if not text:
        return 0
    return len(text.splitlines())


def count_blank_lines(text: str) -> int:
    """Count blank lines in the given text."""
    return sum(1 for line in text.splitlines() if not line.strip())


def count_comment_lines(text: str) -> int:
    """Count comment lines in the given text."""
    count = 0
    in_multiline_string = False
    triple_quotes = ('"""', "'''")

    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            continue

        # Very simple multiline-string tracking for v1.0
        if any(stripped.startswith(q) for q in triple_quotes):
            if sum(stripped.count(q) for q in triple_quotes) == 1:
                in_multiline_string = not in_multiline_string
            count += 1
            continue

        if in_multiline_string:
            count += 1
            if any(q in stripped for q in triple_quotes):
                in_multiline_string = False
            continue

        if stripped.startswith("#"):
            count += 1

    return count