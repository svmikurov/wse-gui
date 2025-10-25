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

from wse.api.schemas.task import (
    Answer,
    Result,
    Question,
)
from .protocol import (
    AssignedServiceProto,
    CalculationServiceProto,
    ExerciseServiceProto,
)
