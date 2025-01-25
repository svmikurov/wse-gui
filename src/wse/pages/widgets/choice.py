"""Custom choice box representation."""

from typing import TypeVar

import toga
from toga.sources import Source, ValueSource
from toga.style import Pack
from toga.widgets.base import StyleT

from wse.pages.widgets.switch import SwitchApp

SourceT = TypeVar('SourceT', bound=Source)


class ChoiceBox(toga.Box):
    """Custom choice box representation."""

    def __init__(
        self,
        text: SourceT | str | None = None,
        style: StyleT | None = None,
        style_switch: StyleT | None = None,
        style_text: StyleT | None = None,
        value: bool | None = None,
        on_change: toga.widgets.switch.OnChangeHandler | None = None,
    ) -> None:
        """Construct the box."""
        super().__init__()
        self.text = text if text else ValueSource()
        self.style = style if style else Pack()
        self._style_switch = style_switch if style_text else Pack()
        self._style_text = style_text if style_text else Pack()
        self.value = value
        self.on_change = on_change

        # Set a dummy handler before installing the actual
        # on_change, because we do not want on_change
        # triggered by the initial value being set.
        self.on_change = None
        self.value = value if value else False
        self.on_change = on_change

        # Widgets
        self._choice_switch = SwitchApp(
            text='',
            style=self._style_switch,
            value=self.value,
            on_change=self.on_change,
        )
        self._choice_text = toga.MultilineTextInput(
            style=self._style_text,
            readonly=True,
        )
        self._choice_text.style.flex = 1

        # DOM
        self.add(self._choice_switch, self._choice_text)

        # Listener
        self.text.add_listener(self)

    #####################################################################
    # Listener method

    def change(self, item: str) -> None:
        """Update choice box text."""
        self._choice_text.value = item
