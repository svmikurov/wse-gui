"""Defines numeric keyboard."""

import toga
from toga.style import Pack

from wse.features.mathem.interface_units.symbol_boxes import (
    ActionButtonBox,
    DigitButtonBox,
    SignButtonBox,
)
from wse.interface.imathem import IButtonBox


class NumericKeypad:
    """Numeric keypad."""

    def __init__(
        self,
        digit_buttons: IButtonBox | None = None,
        sign_buttons: IButtonBox | None = None,
        action_buttons: IButtonBox | None = None,
    ) -> None:
        """Construct the keypad."""
        self._digit_buttons = self._init(digit_buttons, DigitButtonBox())
        self._sign_buttons = self._init(sign_buttons, SignButtonBox())
        self._action_buttons = self._init(action_buttons, ActionButtonBox())

        self._build_keypad_v1()

    def _build_keypad_v1(self) -> None:
        self._keypad_v1 = toga.Box(
            children=[
                toga.Box(
                    style=Pack(direction='column', flex=1),
                    children=[self._sign_buttons.content],
                ),
                toga.Box(
                    style=Pack(direction='column', flex=4),
                    children=[self._digit_buttons.content],
                ),
                toga.Box(
                    style=Pack(direction='column', flex=1),
                    children=[self._action_buttons.content],
                ),
            ]
        )

    @property
    def keypad_v1(self) -> [toga.Widget]:
        """Numeric keypad v1."""
        return self._keypad_v1

    @staticmethod
    def _init(attr: IButtonBox | None, obj: IButtonBox) -> IButtonBox:
        return attr if attr is not None else obj
