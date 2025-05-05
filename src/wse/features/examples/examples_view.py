"""Defines Practice page view."""
import dataclasses

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.enums import StyleID
from wse.features.shared.enums.object_id import ObjectID
from wse.features.shared.ui.ui_text import TitleLabel
from wse.interface.ifeatures import IContent
from wse.interface.iui.ibutton import IButtonHandler


@dataclasses.dataclass
class ExamplesView:
    """Practice page view."""

    _content: IContent
    _style_config: dict
    button_handler: IButtonHandler

    def __post_init__(self) -> None:
        """Post init."""
        self._content.id = ObjectID.PRACTICE
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
            self._back_button,
        )

    def _create_ui(self) -> None:
        # Title
        self._title_label = TitleLabel()

        # Buttons
        self._back_button = self._create_navigation_button()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._title_label.text = _(NavigationID.EXAMPLES)

        # Buttons
        self._back_button.text = _(NavigationID.BACK)

    # Widget style

    @property
    def _ui_styles(self) -> dict[toga.Widget, StyleID]:
        return {
            self._title_label: StyleID.TITLE,
            self._back_button: StyleID.DEFAULT_BUTTON,
        }

    def update_ui_style(self) -> None:
        """Update widgets style."""
        style = self._style_config

        for widget, style_id in self._ui_styles.items():
            widget.style.update(**style.get(style_id))

    # Utility methods

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content

    def _create_navigation_button(self) -> toga.Button:
        return toga.Button(on_press=self.button_handler.navigate)
