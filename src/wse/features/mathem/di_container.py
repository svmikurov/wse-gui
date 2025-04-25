"""Defines dependency injection containers for Mathematical package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigation_id import NavigationID
from wse.features import mathem


class MathematicalContainer(containers.DeclarativeContainer):
    """Mathematical page container."""

    mathematical_model = providers.Factory(
        mathem.MathematicalModel,
    )
    mathematical_view = providers.Factory(
        mathem.MathematicalView,
    )
    mathematical_controller = providers.Factory(
        mathem.MathematicalController,
        model=mathematical_model,
        view=mathematical_view,
    )
    multiplication_model = providers.Factory(
        mathem.MultiplicationModel,
    )
    multiplication_view = providers.Factory(
        mathem.MultiplicationView,
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
