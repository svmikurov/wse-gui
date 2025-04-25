"""Defines examples of Toga widget build."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import examples


class ExamplesContainer(containers.DeclarativeContainer):
    """Toga widget build examples."""

    auth_service = providers.Dependency()
    api_client = providers.Dependency()
    content_box = providers.Dependency()
    subject = providers.Dependency()
    # Containers
    layer_container = providers.DependenciesContainer()

    examples_model = providers.Factory(
        examples.PracticeModel,
        service_layer=layer_container.service_layer,
    )
    examples_view = providers.Factory(
        examples.PracticeView,
    )
    examples_controller = providers.Factory(
        examples.PracticeController,
        model=examples_model,
        view=examples_view,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavigationID.PRACTICE: examples_controller,
        }
    )
