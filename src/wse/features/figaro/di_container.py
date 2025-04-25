"""Defines dependency injection containers for "Figaro" package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import figaro
from wse.features.figaro.containers.swarm_panel import SwarmControlPanel


class FigaroContainer(containers.DeclarativeContainer):
    """Figaro packages container."""

    auth_service = providers.Dependency()
    api_client = providers.Dependency()
    content_box = providers.Dependency()
    subject = providers.Dependency()
    # Containers
    layer_container = providers.DependenciesContainer()

    # Control panel layer
    swarm_panel = providers.Factory(
        SwarmControlPanel,
    )

    # Figaro home page
    figaro_model = providers.Factory(
        figaro.FigaroModel,
        api_client=api_client,
        subject=subject,
    )
    figaro_view = providers.Factory(
        figaro.FigaroView,
        subject=subject,
        content_box=content_box,
    )
    figaro_controller = providers.Factory(
        figaro.FigaroController,
        model=figaro_model,
        view=figaro_view,
    )

    # Swarm page
    swarm_model = providers.Factory(
        figaro.SwarmModel,
        api_client=api_client,
        subject=subject,
    )
    swarm_view = providers.Factory(
        figaro.SwarmView,
        subject=subject,
        content_box=content_box,
        swarm_panel=swarm_panel,
    )
    swarm_controller = providers.Factory(
        figaro.SwarmController,
        model=swarm_model,
        view=swarm_view,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.FIGARO: figaro_controller,
            NavigationID.SWARM: swarm_controller,
        }
    )
