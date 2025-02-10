"""App controllers."""

from wse.controllers.exercise import ControllerExercise
from wse.controllers.form import (
    FormController,
    TermFormController,
    WordFormController,
)
from wse.controllers.main import HomeContr
from wse.controllers.calculations import CalcContr
from wse.controllers.params import ControllerParams
from wse.controllers.table import ControllerTable
from wse.controllers.testing import ControllerTest

__all__ = [
    'ControllerParams',
    'ControllerExercise',
    'ControllerTest',
    'ControllerTable',
    'FormController',
    'WordFormController',
    'TermFormController',
    'CalcContr',
    'HomeContr',
]
