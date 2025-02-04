"""Custom widget for fraction display."""

from typing import TypeVar

import toga
from toga import colors
from toga.constants import RIGHT
from toga.sources import Source
from toga.style import Pack

from wse.pages.widgets.box import BoxFlexCol

SourceT = TypeVar('SourceT', bound=Source)

WIDTH = 50
HEIGHT = 70


class ItemDisplay(toga.TextInput):
    """The item display widget."""

    def __init__(self, source: SourceT | None = None) -> None:
        """Construct the widget."""
        super().__init__()
        self.value = source if source else '123'
        self.readonly = True
        self.style.width = WIDTH
        self.style.text_align = RIGHT


class Fraction(toga.Box):
    """Custom widget for fraction display."""

    def __init__(self) -> None:
        """Construct the widget."""
        super().__init__()
        self.style.flex = 1
        self.style.height = HEIGHT

        # Integer
        _integer = ItemDisplay()
        _box_align_top = BoxFlexCol()
        _box_align_bottom = BoxFlexCol()
        _box_integer = toga.Box(children=[_integer])
        _box_integer_outer = BoxFlexCol(
            style=Pack(width=WIDTH),
            children=[
                _box_align_top,
                _box_integer,
                _box_align_bottom,
            ],
        )

        # Fraction
        _numerator = ItemDisplay()
        _denominator = ItemDisplay()
        _box_numerator = toga.Box(children=[_numerator])
        _box_denominator = toga.Box(children=[_denominator])
        _box_delimiter = toga.Box(
            children=[toga.Divider(style=Pack(background_color=colors.WHITE))]
        )
        _box_fraction_outer = BoxFlexCol(
            style=Pack(width=WIDTH),
            children=[
                _box_numerator,
                _box_delimiter,
                _box_denominator,
            ],
        )

        # DOM
        self.add(
            _box_integer_outer,
            _box_fraction_outer,
        )
