from dataclasses import dataclass, asdict


@dataclass
class CodeStats:
    """
    Stores all statistics collected from a Python file.
    """

    total_lines: int = 0
    blank_lines: int = 0
    comment_lines: int = 0
    code_lines: int = 0

    variables: int = 0
    functions: int = 0
    classes: int = 0
    imports: int = 0

    ifs: int = 0
    elifs: int = 0
    elses: int = 0

    for_loops: int = 0
    while_loops: int = 0

    returns: int = 0

    def to_dict(self) -> dict:
        """Return all stats as a dictionary."""
        return asdict(self)

    def __str__(self) -> str:
        """Simple readable output."""
        return (
            f"CodeStats("
            f"lines={self.total_lines}, "
            f"code={self.code_lines}, "
            f"blank={self.blank_lines}, "
            f"comments={self.comment_lines}, "
            f"functions={self.functions}, "
            f"classes={self.classes}, "
            f"variables={self.variables}, "
            f"imports={self.imports}, "
            f"ifs={self.ifs}, "
            f"elifs={self.elifs}, "
            f"elses={self.elses}, "
            f"for_loops={self.for_loops}, "
            f"while_loops={self.while_loops}, "
            f"returns={self.returns})"
        )