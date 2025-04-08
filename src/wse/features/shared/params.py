"""Defines a params selection (choice) widgets."""

import toga
from toga.style import Pack

from wse.features.shared.base_ui import BaseBox
from wse.features.shared.observer import Subject
from wse.features.shared.text import LabelParam


class SelectionBox(toga.Box):
    """Container containing a selection with a label."""

    label: LabelParam
    _selection: toga.Selection

    def __init__(self, source: Subject, label_text: str | None = None) -> None:
        """Construct the box."""
        super().__init__()
        self.source = source
        self.label_text = label_text or ''

        # Style of the inner widget
        self._inner_style = Pack(padding=(2, 0, 2, 0))

        # Add UI
        self._create_ui()
        self._add_ui()

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
