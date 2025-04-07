"""Defines dependency injection containers for foreign package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features.foreign import (
    ForeignController,
    ForeignView,
    ParamsController,
    ParamsView,
    TasksController,
    TasksView,
)


class ForeignContainer(containers.DeclarativeContainer):
    """Foreign pages container."""

    content_box = providers.Dependency()

    # Foreign home page
    home_view = providers.Factory(ForeignView, content_box=content_box)
    home_controller = providers.Factory(ForeignController, view=home_view)

    # Foreign tasks page
    tasks_view = providers.Factory(TasksView, content_box=content_box)
    tasks_controller = providers.Factory(TasksController, view=tasks_view)

    # Foreign params page
    params_view = providers.Factory(ParamsView, content_box=content_box)
    params_controller = providers.Factory(ParamsController, view=params_view)

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.FOREIGN: home_controller,
            NavigationID.FOREIGN_TASKS: tasks_controller,
            NavigationID.FOREIGN_PARAMS: params_controller,
        }
    )
