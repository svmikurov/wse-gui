"""Calculation exercise."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CalculationExercise:
    """Calculation exercise."""

    # TODO: Remove exercise name default value
    name: str = 'multiplication'
    min_value = '1'
    max_value = '9'
    question_url_path: str = '/api/v1/math/exercise/calculation/'
    check_url_path: str = 'api/v1/math/exercise/calculation/validate/'
    task_io: str = 'text'
