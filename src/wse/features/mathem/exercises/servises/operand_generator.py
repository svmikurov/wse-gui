"""Defines generation math exercises operands."""

from random import randint

from wse.features.mathem.interfaces.iservices import (
    IOperandGenerator,
)


class RandomOperandGenerator(IOperandGenerator):
    """Random generator of integer operands within configured range."""

    @staticmethod
    def generate(min_value: int, max_value: int) -> int:
        """Generate random integer within configured range."""
        return randint(min_value, max_value)
