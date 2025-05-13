"""Defines Practice page view."""

import dataclasses

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavID
from wse.features.shared.enums import StyleID
from wse.features.shared.enums.object_id import ObjectID
from wse.interfaces.ifeatures.icontent import IContent
from wse.interfaces.iui.ibutton import IButtonHandler


@dataclasses.dataclass
class ExamplesView:
    """Practice page view."""

    _content: IContent
    _style_config: dict
    button_handler: IButtonHandler

    def __post_init__(self) -> None:
        """Post init."""
        self._content.id = ObjectID.EXAMPLES
        self._layout_view()

    def _layout_view(self) -> None:
        self._create_ui()
        self._populate_content()
        self.update_ui_style()
        self.localize_ui()

    def _populate_content(self) -> None:
        self.content.add(
            self._title_label,
            toga.Box(style=Pack(flex=1)),  # Flex stub
            self._btn_goto_table_source,
            self._btn_goto_selections,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        # Title
        self._title_label = toga.Label('')

        # Buttons
        self._btn_goto_selections = self._create_nav_btn()
        self._btn_goto_table_source = self._create_nav_btn()
        self._btn_back = self._create_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._title_label.text = _(NavID.EXAMPLES)

        # Buttons
        self._btn_goto_selections.text = _(NavID.EXAMPLES_SELECTION)
        self._btn_goto_table_source.text = _(NavID.EXAMPLES_TABLE_SOURCE)
        self._btn_back.text = _(NavID.BACK)

    # Widget style

    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]:
        return {
            self._title_label: StyleID.TITLE,
            self._btn_goto_selections: StyleID.DEFAULT_BUTTON,
            self._btn_goto_table_source: StyleID.DEFAULT_BUTTON,
            self._btn_back: StyleID.DEFAULT_BUTTON,
        }

    def update_ui_style(self) -> None:
        """Update widgets style."""
        for widget, style_id in self._ui_styles.items():
            widget.style.update(**self._style_config.get(style_id))

    # Utility methods

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content

    def _create_nav_btn(self) -> toga.Button:
        return toga.Button(on_press=self.button_handler.navigate)
