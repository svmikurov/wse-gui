"""Mathematical exercises."""

from wse.features.mathem.exercises.answer_checker import AnswerChecker, Result
from wse.features.mathem.exercises.exercises import MultiplicationExercise
from wse.features.mathem.exercises.render import TextDisplayRenderer
from wse.features.mathem.exercises.storage import TaskStorage

__all__ = [
    'AnswerChecker',
    'Result',
    'MultiplicationExercise',
    'TaskStorage',
    'TextDisplayRenderer',
]
