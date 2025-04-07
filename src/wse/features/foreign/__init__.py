"""Foreign pages package."""

from wse.features.foreign.home_controller import ForeignController
from wse.features.foreign.home_view import ForeignView
from wse.features.foreign.tasks_controller import TasksController
from wse.features.foreign.tasks_view import TasksView

__all__ = [
    'ForeignController',
    'ForeignView',
    'TasksController',
    'TasksView',
]
