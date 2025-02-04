"""App controllers."""

from wse.contr.exercise import ControllerExercise
from wse.contr.form import (
    FormController,
    TermFormController,
    WordFormController,
)
from wse.contr.main import MainContr
from wse.contr.multiplication import MultContr
from wse.contr.params import ControllerParams
from wse.contr.table import ControllerTable
from wse.contr.testing import ControllerTest

__all__ = [
    'ControllerParams',
    'ControllerExercise',
    'ControllerTest',
    'ControllerTable',
    'FormController',
    'WordFormController',
    'TermFormController',
    'MultContr',
    'MainContr',
]
