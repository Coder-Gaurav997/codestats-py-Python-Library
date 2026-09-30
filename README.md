# PyCodeStats

PyCodeStats is a small Python library for collecting basic statistics from Python files.

## Features

* Total lines
* Blank lines
* Comment lines
* Code lines
* Variables
* Functions
* Classes
* Imports
* `if` / `elif` / `else`
* `for` loops
* `while` loops
* `return` statements

## Install

```bash
pip install codestats-py
```

## Usage

```python
import codestats as cs

stats = cs.analyze("main.py")
print(stats)
```

## Access individual stats

```python
import codestats as cs

stats = cs.analyze("main.py")

print(stats.total_lines)
print(stats.functions)
print(stats.classes)
print(stats.variables)
print(stats.for_loops)
print(stats.while_loops)
```

## Pretty report

```python
import codestats as cs

cs.report("main.py")
```

## Example output

```text
==============================
        PYCODESTATS
==============================

Total Lines     : 120
Blank Lines     : 18
Comment Lines   : 9
Code Lines      : 102

Variables       : 15
Functions       : 4
Classes         : 2
Imports         : 3

If              : 6
Elif            : 2
Else            : 3

For Loops       : 5
While Loops     : 1

Returns         : 7

==============================
```

## API

### `analyze(file_path)`

Returns one `CodeStats` object containing all counts.

### `report(file_path)`

Prints a formatted report and also returns it as a string.

## Planned future versions

* Directory analysis
* JSON export
* CSV export
* CLI
* More metrics

## License

MIT