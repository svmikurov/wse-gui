"""Defines examples of Toga widget build."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavID
from wse.features import examples


class ExamplesContainer(containers.DeclarativeContainer):
    """Toga widget build examples."""

    # Dependencies
    content = providers.Dependency()
    subject = providers.Dependency()
    style_config = providers.Dependency()
    button_handler = providers.Dependency()

    # Container dependencies
    share_container = providers.DependenciesContainer()

    # -=== Pages ===-
    # Home page
    examples_view = providers.Factory(
        examples.ExamplesView,
        _content=content,
        _style_config=style_config,
        button_handler=button_handler,
    )
    examples_controller = providers.Factory(
        examples.ExamplesController,
        view=examples_view,
        _subject=subject,
    )

    # Selection
    selection_view = providers.Factory(
        examples.SelectionView,
        content=content,
        style_config=style_config,
        button_handler=button_handler,
    )
    selection_controller = providers.Factory(
        examples.SelectionController,
        view=selection_view,
        _subject=subject,
    )

    # NavigationID routes
    routes = providers.Dict(
        {
            NavID.EXAMPLES: examples_controller,
            NavID.EXAMPLES_SELECTION: selection_controller,
        }
    )
