"""Defines dependency injection containers for interface units."""

from dependency_injector import containers, providers

from wse.features.mathem.interface_units import (
    ActionButtonBox,
    DigitButtonBox,
    NumericKeypad,
    SignButtonBox,
)


class MathematicalUnitsContainer(containers.DeclarativeContainer):
    """Mathematical interface units container."""

    digit_buttons = providers.Factory(DigitButtonBox)
    sign_buttons = providers.Factory(SignButtonBox)
    action_buttons = providers.Factory(ActionButtonBox)

    numeric_keypad = providers.Factory(
        NumericKeypad,
        digit_buttons=digit_buttons,
        sign_buttons=sign_buttons,
        action_buttons=action_buttons,
    )
