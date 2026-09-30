"""
PyCodeStats
===========

A small Python library for collecting basic code statistics from Python files.

Public API:
- analyze(path): return a CodeStats object
- report(path): print a formatted report
"""

from .models import CodeStats
from .analyzer import analyze
from .report import report

__version__ = "1.0.0"

__all__ = [
    "CodeStats",
    "analyze",
    "report",
    "__version__",
]