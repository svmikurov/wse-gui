"""Defines protocols for math exercises services."""

from typing import Protocol


class IOperandGenerator(Protocol):
    """Protocol for random generator of integer operands."""

    @staticmethod
    def generate(min_value: int, max_value: int) -> int:
        """Generate random integer within configured range."""
