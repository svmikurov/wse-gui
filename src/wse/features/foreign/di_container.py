"""Defines dependency injection containers for foreign package."""

from dependency_injector import containers, providers

from wse.core.navigaion.navigation_id import NavigationID
from wse.features.foreign.home_controller import ForeignController
from wse.features.foreign.home_view import ForeignView
from wse.features.foreign.tasks_controller import TasksController
from wse.features.foreign.tasks_view import TasksView


class ForeignContainer(containers.DeclarativeContainer):
    """Foreign pages container."""

    content_box = providers.Dependency()

    # Foreign home page
    home_view = providers.Factory(ForeignView, content_box=content_box)
    home_controller = providers.Factory(ForeignController, view=home_view)

    # Foreign tasks page
    tasks_view = providers.Factory(TasksView, content_box=content_box)
    tasks_controller = providers.Factory(TasksController, view=tasks_view)

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.FOREIGN: home_controller,
            NavigationID.FOREIGN_TASKS: tasks_controller,
        }
    )
