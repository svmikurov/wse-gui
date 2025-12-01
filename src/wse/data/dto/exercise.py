"""Calculation exercise."""

from dataclasses import dataclass, field

from wse_exercises.core import MathEnum

AVAILABLE_EXERCISES = [
    MathEnum.ADDING,
    MathEnum.SUBTRACTION,
    MathEnum.MULTIPLICATION,
    MathEnum.DIVISION,
]


def get_available_exercises() -> list[MathEnum]:
    """Return available exercise enumeration."""
    return AVAILABLE_EXERCISES


@dataclass(frozen=True)
class CalculationExercise:
    """Calculation exercise."""

    exercises: list[MathEnum] = field(default_factory=get_available_exercises)
    default: MathEnum = MathEnum.DIVISION
    current: MathEnum = MathEnum.DIVISION

    min_value: str = '1'
    max_value: str = '9'

    question_url_path: str = '/api/v1/math/exercise/calculation/'
    check_url_path: str = 'api/v1/math/exercise/calculation/validate/'

    task_io: str = 'text'
