"""Custom choice box representation."""

from typing import TypeVar

import toga
from toga.sources import Source
from toga.style import Pack
from toga.widgets.base import StyleT

from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.switch import SwitchApp

SourceT = TypeVar('SourceT', bound=Source)

WIDTH = 70


class ItemDisplay(toga.TextInput):
    """The item display widget."""

    def __init__(self, source: SourceT | None = None) -> None:
        """Construct the widget."""
        super().__init__()
        self.value = source if source else '123'
        self.readonly = True
        self.style.flex = 1


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
        self.style.flex = 1
        self.on_change = on_change

        # Switch
        _choice_switch = SwitchApp(
            text='',
            on_change=self.on_change,
        )
        _box_align_top = BoxFlexCol()
        _box_align_bottom = BoxFlexCol()
        _box_switch = toga.Box(children=[_choice_switch])
        _box_switch_outer = BoxFlexCol(
            style=Pack(width=WIDTH),
            children=[
                _box_align_top,
                _box_switch,
                _box_align_bottom,
            ],
        )

        # Text
        self._text_line1 = ItemDisplay()
        self._text_line2 = ItemDisplay()
        _box_line1 = toga.Box(children=[self._text_line1])
        _box_line2 = toga.Box(children=[self._text_line2])
        _box_text_outer = BoxFlexCol(
            children=[
                _box_line1,
                _box_line2,
            ],
        )

        # DOM
        self.add(
            _box_switch_outer,
            _box_text_outer,
        )

    #####################################################################
    # Listener method

    def change(self, item: list[str, str]) -> None:
        """Update choice box text."""
        # item_line1, item_line2 = item
        self._text_line1.value = 'item_line1'
        self._text_line2.value = 'item_line2'
