"""Foreign pages package."""

from wse.features.foreign.foreign_controller import ForeignController
from wse.features.foreign.foreign_view import ForeignView
from wse.features.foreign.params_controller import ParamsController
from wse.features.foreign.params_view import ParamsView
from wse.features.foreign.tasks_controller import TasksController
from wse.features.foreign.tasks_view import TasksView

__all__ = [
    'ForeignController',
    'ForeignView',
    'ParamsController',
    'ParamsView',
    'TasksController',
    'TasksView',
]
