"""
report.py
---------

Creates a clean, human-readable report from CodeStats.
"""

from .analyzer import analyze
from .models import CodeStats


def format_report(stats: CodeStats) -> str:
    """Build a pretty multi-line report from the given stats object."""
    lines = [
        "==============================",
        "        PYCODESTATS",
        "==============================",
        "",
        f"Total Lines     : {stats.total_lines}",
        f"Blank Lines     : {stats.blank_lines}",
        f"Code Lines      : {stats.code_lines}",
        f"Comment Lines   : {stats.comment_lines}",
        "",
        f"Variables       : {stats.variables}",
        f"Functions       : {stats.functions}",
        f"Classes         : {stats.classes}",
        f"Imports         : {stats.imports}",
        "",
        f"If              : {stats.ifs}",
        f"Elif            : {stats.elifs}",
        f"Else            : {stats.elses}",
        "",
        f"For Loops       : {stats.for_loops}",
        f"While Loops     : {stats.while_loops}",
        "",
        f"Returns         : {stats.returns}",
        "",
        "==============================",
    ]
    return "\n".join(lines)


def report(file_path: str) -> str:
    """
    Analyze a Python file and print a formatted report.

    Returns the report text too, so the user can reuse it.
    """
    stats = analyze(file_path)
    output = format_report(stats)
    print(output)
    return output