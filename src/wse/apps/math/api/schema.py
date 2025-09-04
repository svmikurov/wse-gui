"""Defines Math app schema."""

from wse.apps.main.api.schema import ExerciseMeta
from wse.feature.base import BaseSchema


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
