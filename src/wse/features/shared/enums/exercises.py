"""Defines enumeration of available exercise types."""

from wse.core.base import BaseEnum


class Exercises(BaseEnum):
    """Enumeration of available exercise types."""

    ADDING = 'adding'
    DIVISION = 'division'
    MULTIPLICATION = 'multiplication'
    SUBTRACTION = 'subtraction'
