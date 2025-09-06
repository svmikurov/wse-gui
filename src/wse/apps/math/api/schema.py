"""Defines Math app schema."""

from wse.feature.base import BaseSchema
from wse.feature.shared.schemas.exercise import ExerciseMeta


class CalculationConfig(BaseSchema):
    """Types for calculation exercise config."""

    min_value: str
    max_value: str


class CalculationCondition(BaseSchema):
    """Calculation exercise condition data."""

    exercise_name: str
    config: CalculationConfig


class Calculation(ExerciseMeta):
    """Calculation exercise data."""

    condition: CalculationCondition
