"""Defines a params selection (choice) widgets."""

from typing import Callable

import toga
from toga.style import Pack

from wse.features.shared.observer import Subject
from wse.features.shared.ui_containers import (
    ColumnFlexBox,
    RowBox,
    RowFlexBox,
)

# Labeled widget padding style
LABEL_PADDING = (0, 0, 0, 0)
SWITCH_PADDING = (0, 6, 0, 0)
WIDGET_PADDING = (0, 0, 0, 0)
OUTER_BOX_PADDING = (2, 6, 2, 6)


def wrap_in_box(
    widget: toga.Widget,
    box_style: Pack,
    box: toga.Box | None = None,
) -> toga.Box:
    """Wrap the widget to styled box."""
    box = box or ColumnFlexBox
    return box(style=box_style, children=[widget])


class LayoutWidgetLabel:
    """Layout of widget with label."""

    _label: toga.Label
    _label_box_style: Pack
    widget: toga.Widget
    _widget_box_style: Pack

    # Multiply inherit methods
    add: Callable

    def _layout_boxes(self) -> None:
        self.add(
            wrap_in_box(self._label, self._label_box_style),
            wrap_in_box(self.widget, self._widget_box_style),
        )


class WrapSwitchWidgetLabelMixin:
    """Wrapped switch and widget with label."""

    _label: toga.Label
    _label_box_style: Pack
    switch: toga.Switch
    _switch_box_style: Pack
    widget: toga.Widget
    _widget_box_style: Pack

    # Multiply inherit methods
    add: Callable

    def _layout_boxes(self) -> None:
        self.add(
            RowFlexBox(
                children=[
                    RowFlexBox(
                        style=self._label_box_style,
                        children=[self._label],
                    ),
                    RowBox(
                        style=self._switch_box_style,
                        children=[self.switch],
                    ),
                ]
            ),
            ColumnFlexBox(
                style=self._widget_box_style, children=[self.widget]
            ),
        )


class WidgetLabel(toga.Box):
    """Base container containing a widget with a label."""

    text: str

    # Override in children class
    _widget_class: Callable

    # Class attributes
    _label_box_style = Pack(
        padding=LABEL_PADDING,
    )
    _widget_box_style = Pack(
        padding=WIDGET_PADDING,
    )
    _box_style = Pack(
        padding=OUTER_BOX_PADDING,
    )

    # Multiply inherit methods
    _layout_boxes: Callable

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__()
        self._source = source or Subject()
        self._label = toga.Label(text='')

        # Box layout
        self.style = self._box_style
        self._layout_boxes()

    @property
    def widget(self) -> toga.Widget:
        """Create widget class instance (read-only)."""
        if hasattr(self._widget_class, 'text'):
            return self._widget_class(text='')
        return self._widget_class()

    @property
    def text(self) -> str:
        """Widget label text."""
        return self._label.text

    @text.setter
    def text(self, value: str) -> None:
        self._label.text = value


class SwitchWidgetLabel(WidgetLabel):
    """Base container containing a widget and switch with a label."""

    # Class attributes
    _switch: toga.Switch
    _switch_box_style = Pack(
        padding=SWITCH_PADDING,
    )

    @property
    def switch(self) -> toga.Switch:
        """Create switch instance (read-only)."""
        return toga.Switch(text='')


class WidgetLabelBox(LayoutWidgetLabel, WidgetLabel):
    """Container containing a base widget with a label."""


class SwitchWidgetLabelBox(WrapSwitchWidgetLabelMixin, SwitchWidgetLabel):
    """Container containing a switch with a label."""


class SelectionLabelBox(WidgetLabelBox):
    """Container containing a selection with a label."""

    _widget_class = toga.Selection


class SwitchLabelBox(WidgetLabelBox):
    """Container containing a switch with a label."""

    _widget_class = toga.Switch


class SwitchNumberInputBox(SwitchWidgetLabelBox):
    """Container containing a switch and number input with a label."""

    _widget_class = toga.NumberInput


class ProgressBox(ColumnFlexBox):
    """Container containing a switches with a label."""

    study: SwitchLabelBox
    examination: SwitchLabelBox
    repeat: SwitchLabelBox
    know: SwitchLabelBox

    _widget_row_style = Pack(padding=(0, 0, 8, 0))
    _switch_box_style = Pack()

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__()
        self._source = source or Subject()

        # Box layout
        self._create_widgets()
        self._layout_boxes()

    def _layout_boxes(self) -> None:
        self.add(
            RowBox(
                style=self._widget_row_style,
                children=[
                    wrap_in_box(self.study, self._switch_box_style),
                    wrap_in_box(self.repeat, self._switch_box_style),
                ],
            ),
            RowBox(
                style=self._widget_row_style,
                children=[
                    wrap_in_box(self.examination, self._switch_box_style),
                    wrap_in_box(self.know, self._switch_box_style),
                ],
            ),
        )

    def _create_widgets(self) -> None:
        self.study = SwitchLabelBox()
        self.examination = SwitchLabelBox()
        self.repeat = SwitchLabelBox()
        self.know = SwitchLabelBox()
