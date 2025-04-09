"""Defines a params selection (choice) widgets."""

import toga
from toga.constants import COLUMN
from toga.style import Pack

from wse.features.base.ui_params import BaseParamsWidget
from wse.features.shared.observer import Subject
from wse.features.shared.switch import SwitchApp
from wse.features.shared.ui_containers import (
    BaseBox,
    ColumnFlexBox,
    RowBox,
    RowFlexBox,
)
from wse.features.shared.ui_text import LabelParam


class CreateBoxMixin:
    """Mixin to create box for widget place."""

    _inner_style: Pack

    def _create_box(self, inner_widget: toga.Widget) -> toga.Box:
        return BaseBox(style=self._inner_style, children=[inner_widget])


class LabelTextMixin:
    """Mixin adds label text property."""

    _label: LabelParam

    @property
    def text(self) -> str:
        """Label text."""
        return self._label.text

    @text.setter
    def text(self, value: str) -> None:
        self._label.text = value


class SelectionBox(CreateBoxMixin, LabelTextMixin, BaseParamsWidget):
    """Container containing a selection with a label."""

    text: str
    _label: LabelParam
    _selection: toga.Selection

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__(source)

    def _add_ui(self) -> None:
        self.add(
            self._create_box(inner_widget=self._label),
            self._create_box(inner_widget=self._selection),
        )

    def _create_ui(self) -> None:
        self._label = LabelParam('')
        self._selection = toga.Selection()


class SwitchNumberInputBox(LabelTextMixin, BaseParamsWidget):
    """Container containing a switch and number input with a label."""

    text: str
    _label: LabelParam
    _switch: SwitchApp
    _number_input: toga.NumberInput

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__(source)

    def _add_ui(self) -> None:
        self.add(
            RowFlexBox(
                children=[
                    RowFlexBox(
                        style=Pack(padding=(2, 0, 2, 2)),
                        children=[self._label],
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
        self._label = LabelParam('')
        self._switch = SwitchApp('')
        self._number_input = toga.NumberInput()


class SwitchBox(CreateBoxMixin, LabelTextMixin, BaseParamsWidget):
    """Container containing a switch and number input with a label."""

    text: str
    _label: LabelParam
    _switch: SwitchApp

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__(source)

    def _add_ui(self) -> None:
        self.add(
            self._create_box(inner_widget=self._label),
            self._create_box(inner_widget=self._switch),
        )

    def _create_ui(self) -> None:
        self._label = LabelParam('')
        self._switch = SwitchApp('')


class ProgressBox(BaseParamsWidget):
    """Container containing a switches with a label."""

    study: SwitchBox
    examination: SwitchBox
    repeat: SwitchBox
    know: SwitchBox

    def __init__(self, source: Subject | None = None) -> None:
        """Construct the box."""
        super().__init__(source)
        self.style.direction = COLUMN

    def _add_ui(self) -> None:
        self.add(
            RowBox(
                children=[
                    self._create_box(inner_widget=self.study),
                    self._create_box(inner_widget=self.repeat),
                ]
            ),
            RowBox(
                children=[
                    self._create_box(inner_widget=self.examination),
                    self._create_box(inner_widget=self.know),
                ]
            ),
        )

    def _create_ui(self) -> None:
        self.study = SwitchBox()
        self.examination = SwitchBox()
        self.repeat = SwitchBox()
        self.know = SwitchBox()

    @staticmethod
    def _create_box(inner_widget: toga.Widget) -> toga.Box:
        return ColumnFlexBox(
            style=Pack(padding_right=4),
            children=[inner_widget],
        )
