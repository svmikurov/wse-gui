"""Abstract base classes for Math discipline API clients."""

from abc import ABC

from ..main.abc import ExerciseApiABC
from . import schemas


class CalculationApiABC(
    ExerciseApiABC[schemas.Calculation],
    ABC,
):
    """ABC for Exercise API client."""
