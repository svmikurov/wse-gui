"""Custom choice box representation."""

from typing import TypeVar

import toga
from toga.sources import Source
from toga.widgets.base import StyleT

from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.switch import SwitchApp

SourceT = TypeVar('SourceT', bound=Source)


class ChoiceBox(toga.Box):
    """Custom choice box representation."""

    def __init__(
        self,
        style_switch: StyleT | None = None,
        style_text: StyleT | None = None,
        on_change: toga.widgets.switch.OnChangeHandler | None = None,
    ) -> None:
        """Construct the box."""
        super().__init__()
        self.style.flex = 1
        self.style_switch = style_switch
        self.style_text = style_text
        self.on_change = on_change

        # Switch
        _box_align_top = BoxFlexCol()
        _box_align_bottom = BoxFlexCol()
        _choice_switch = SwitchApp(
            text='',
            on_change=self.on_change,
        )
        _box_switch = toga.Box(children=[_choice_switch])
        self._box_switch_outer = BoxFlexCol(
            style=self.style_switch,
            children=[
                _box_align_top,
                _box_switch,
                _box_align_bottom,
            ],
        )

        # Text
        self._box_text_outer = BoxFlexCol()

        # DOM
        self.add(
            self._box_switch_outer,
            self._box_text_outer,
        )

    #####################################################################
    # Listener method

    def change(self, item: str) -> None:
        """Update choice box text."""
        self._add_text_line(item)

    def _add_text_line(self, text: str) -> None:
        choice_text = toga.Box(
            children=[
                toga.MultilineTextInput(
                    style=self.style_text,
                    value=text,
                    readonly=True,
                )
            ],
        )
        self._box_text_outer.add(choice_text)
