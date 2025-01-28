"""Custom choice box representation."""

import toga
from toga.style import Pack
from toga.widgets.base import StyleT

from wse.pages.widgets.switch import SwitchApp


class ChoiceBox(toga.Box):
    """Custom choice box representation."""

    def __init__(
        self,
        style: StyleT | None = None,
        style_switch: StyleT | None = None,
        style_text: StyleT | None = None,
        on_change: toga.widgets.switch.OnChangeHandler | None = None,
    ) -> None:
        """Construct the box."""
        super().__init__()
        # Box
        self.style = style if style else Pack()
        # Switch
        self._style_switch = style_switch if style_text else Pack()
        self.on_change = on_change
        # MultilineTextInput
        self._style_text = style_text if style_text else Pack()

        # Widgets
        self._choice_switch = SwitchApp(
            text='',
            style=self._style_switch,
            on_change=self.on_change,
        )
        self._choice_text = toga.MultilineTextInput(
            style=self._style_text,
            readonly=True,
        )
        self._choice_text.style.flex = 1

        # DOM
        self.add(_box_switch, _box_text)
        _box_switch.add(self._choice_switch)
        _box_text.add(self._choice_text)

    #####################################################################
    # Listener method

    def change(self, item: str) -> None:
        """Update choice box text."""
        self._choice_text.value = item
