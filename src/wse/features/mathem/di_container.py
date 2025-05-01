"""Defines dependency injection containers for Mathematical package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import mathem


class MathematicalContainer(containers.DeclarativeContainer):
    """Mathematical page container."""

    # Container dependencies
    share_container = providers.DependenciesContainer()

    # Mathematical page
    mathematical_model = providers.Factory(
        mathem.MathematicalModel,
    )
    mathematical_view = providers.Factory(
        mathem.MathematicalView,
        content_box=share_container.simple_content,
    )
    mathematical_controller = providers.Factory(
        mathem.MathematicalController,
        model=mathematical_model,
        view=mathematical_view,
    )

    # Multiplication page
    multiplication_model = providers.Factory(
        mathem.MultiplicationModel,
    )
    multiplication_view = providers.Factory(
        mathem.MultiplicationView,
        content=share_container.simple_content,
        subject=share_container.subject,
        model_display=share_container.single_line_display,
        input_display=share_container.single_line_display,
        keypad=share_container.digit_keypad,
        style_config=share_container.style_config,
    )
    multiplication_controller = providers.Factory(
        mathem.MultiplicationController,
        model=multiplication_model,
        view=multiplication_view,
    )

    routes = providers.Dict(
        {
            NavigationID.MATHEMATICAL: mathematical_controller,
            NavigationID.MULTIPLICATION: multiplication_controller,
        }
    )
