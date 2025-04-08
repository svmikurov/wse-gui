"""Defines a params selection (choice) widgets."""

from abc import ABC, abstractmethod

import toga
from toga.style import Pack

from wse.features.shared.base_ui import BaseBox, RowBox, ColumnBox, \
    ColumnFlexBox, RowFlexBox
from wse.features.shared.observer import Subject
from wse.features.shared.text import LabelParam


class BaseParamsWidget(toga.Box, ABC):
    """Base container for params element."""

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__()
        self._source = source or Subject()

        # Style of the inner widget
        self._inner_style = Pack(padding=(2, 0, 2, 0))

        # Add UI
        self._create_ui()
        self._add_ui()

    @abstractmethod
    def _add_ui(self) -> None: ...

    @abstractmethod
    def _create_ui(self) -> None: ...


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
                        children=[self._switch]
                    ),
                ]
            ),
            ColumnFlexBox(
                style=self._inner_style,
                children=[self._number_input]),
        )

    def _create_ui(self) -> None:
        self.label = LabelParam('')
        self._switch = toga.Switch('')
        self._number_input = toga.NumberInput()
