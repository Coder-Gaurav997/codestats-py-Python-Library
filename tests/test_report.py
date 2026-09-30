import pytest

from codestats.report import report

def test_report_counts_basic_metrics(tmp_path):
    code = """
import os

x = 1
y = 2

def add(a, b):
    return a + b

class Demo:
    pass

if x > 0:
    print("positive")
else:
    print("non-positive")

for i in range(3):
    print(i)

while x < 5:
    x += 1
"""

    file_path = tmp_path / "sample.py"
    file_path.write_text(code, encoding="utf-8")

    stats = report(str(file_path))

    assert stats.total_lines == 22
    assert stats.blank_lines == 7
    assert stats.code_lines == 15
    assert stats.comment_lines == 0

    assert stats.imports == 1
    assert stats.variables == 3
    assert stats.functions == 1
    assert stats.classes == 1

    assert stats.ifs == 1
    assert stats.elifs == 0
    assert stats.elses == 1

    assert stats.for_loops == 1
    assert stats.while_loops == 1
    assert stats.returns == 1


def test_report_rejects_missing_file():
    with pytest.raises(FileNotFoundError):
        report("does_not_exist.py")