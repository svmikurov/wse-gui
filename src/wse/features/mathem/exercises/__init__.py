"""Mathematical exercises."""

from wse.features.mathem.exercises.checker import AnswerChecker
from wse.features.mathem.exercises.exercises import MultiplicationExercise
from wse.features.mathem.exercises.render import ExerciseRenderer
from wse.features.mathem.exercises.result import CheckResult
from wse.features.mathem.exercises.storage import TaskConditionsStorage

__all__ = [
    'AnswerChecker',
    'CheckResult',
    'ExerciseRenderer',
    'MultiplicationExercise',
    'TaskConditionsStorage',
]
