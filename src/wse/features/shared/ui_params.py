"""Defines a params selection (choice) widgets."""

import toga
from toga.style import Pack

from wse.features.base.ui_params import BaseParamsWidget
from wse.features.shared.observer import Subject
from wse.features.shared.ui_containers import (
    BaseBox,
    ColumnFlexBox,
    RowBox,
    RowFlexBox,
)
from wse.features.shared.ui_text import LabelParam


class SelectionBox(BaseParamsWidget):
    """Container containing a selection with a label."""

    label: LabelParam
    _selection: toga.Selection

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__(source)

    def _add_ui(self) -> None:
        self.add(
            self._create_box(inner_widget=self.label),
            self._create_box(inner_widget=self._selection),
        )

    def _create_ui(self) -> None:
        self.label = LabelParam('')
        self._selection = toga.Selection()

    def _create_box(self, inner_widget: toga.Widget) -> toga.Box:
        return BaseBox(style=self._inner_style, children=[inner_widget])


class SwitchNumberInputBox(BaseParamsWidget):
    """Container containing a switch and number input with a label."""

    label: LabelParam
    _switch: toga.Switch
    _number_input: toga.NumberInput

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__(source)

    def _add_ui(self) -> None:
        self.add(
            RowFlexBox(
                children=[
                    RowFlexBox(
                        style=self._inner_style,
                        children=[self.label],
                    ),
                    RowBox(
                        style=Pack(padding=(2, 6, 2, 0)),
                        children=[self._switch],
                    ),
                ]
            ),
            ColumnFlexBox(
                style=self._inner_style, children=[self._number_input]
            ),
        )

    def _create_ui(self) -> None:
        self.label = LabelParam('')
        self._switch = toga.Switch('')
        self._number_input = toga.NumberInput()
