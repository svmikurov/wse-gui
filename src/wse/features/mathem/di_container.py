"""Defines dependency injection containers for Mathematical package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import mathem
from wse.features.mathem.interface_units.di_container import (
    MathematicalUnitsContainer,
)
from wse.features.shared.content import SimpleContent


class MathematicalContainer(containers.DeclarativeContainer):
    """Mathematical page container."""

    # Containers
    mathematical_units = providers.Container(MathematicalUnitsContainer)

    # Providers
    simple_content = providers.Factory(SimpleContent)

    # Mathematical page
    mathematical_model = providers.Factory(
        mathem.MathematicalModel,
    )
    mathematical_view = providers.Factory(
        mathem.MathematicalView,
        content_box=simple_content,
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
        numeric_keypad=mathematical_units.numeric_keypad,
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
