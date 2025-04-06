"""Defines dependency injection containers for foreign package."""

from dependency_injector import containers, providers

from wse.features.foreign.home_ctrl import ForeignCtrl
from wse.features.foreign.home_view import ForeignView
from wse.features.foreign.tasks_ctrl import TasksController
from wse.features.foreign.tasks_view import TasksView
from wse.features.shared.button_text import ButtonText


class ForeignContainer(containers.DeclarativeContainer):
    """Foreign pages container."""

    content_box = providers.Dependency()

    # Foreign home page
    home_view = providers.Factory(ForeignView, content_box=content_box)
    home_ctrl = providers.Factory(ForeignCtrl, view=home_view)

    # Foreign tasks page
    tasks_view = providers.Factory(TasksView, content_box=content_box)
    tasks_ctrl = providers.Factory(TasksController, view=tasks_view)

    # Navigation routes
    routes = providers.Dict(
        {
            ButtonText.FOREIGN: home_ctrl,
            ButtonText.FOREIGN_TASKS: tasks_ctrl,
        }
    )
