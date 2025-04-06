"""Defines dependency injection containers for foreign package."""

from dependency_injector import containers, providers

from wse.features.foreign.home_ctrl import ForeignCtrl
from wse.features.foreign.home_view import ForeignView
from wse.features.foreign.tasks_ctrl import TasksController
from wse.features.foreign.tasks_view import TasksView


class ForeignContainer(containers.DeclarativeContainer):
    """Foreign pages container."""

    content_box = providers.Dependency()

    home_view = providers.Factory(ForeignView, content_box=content_box)
    home_ctrl = providers.Factory(ForeignCtrl, view=home_view)

    tasks_view = providers.Factory(TasksView, content_box=content_box)
    tasks_ctrl = providers.Factory(TasksController, view=tasks_view)
