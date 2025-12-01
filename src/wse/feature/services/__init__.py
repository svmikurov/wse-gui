"""Defines services for features."""

__all__ = [
    'ExerciseServiceProto',
    'AssignedServiceProto',
    'CalculationServiceProto',
]

from .protocol import (
    AssignedServiceProto,
    CalculationServiceProto,
    ExerciseServiceProto,
)
