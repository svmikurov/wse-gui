"""Defines services for features."""

__all__ = [
    # Entry
    'Question',
    'Answer',
    'Result',
    # Service
    'ExerciseServiceProto',
    'AssignedServiceProto',
    'CalculationServiceProto',
]

from .schema import (
    Answer,
    Result,
    Question,
)
from .protocol import (
    AssignedServiceProto,
    CalculationServiceProto,
    ExerciseServiceProto,
)
