"""Defines Math app api protocol."""

from typing import Protocol

from wse.core.api.protocol import ExerciseApiProto

from . import Calculation


class CalculationApiProto(
    ExerciseApiProto[Calculation],
    Protocol,
):
    """Protocol for exercise API client interface."""
