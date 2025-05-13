"""Defines Figaro page view."""

import toga

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc import BaseView
from wse.features.shared.enums.object_id import ObjectID
from wse.features.shared.ui.ui_text import TextPanel, TitleLabel


class FigaroView(BaseView):
    """Figaro page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.FIGARO

        # Construct UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self.text_panel,
            self._btn_swarm,
            self._btn_home,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel()

        # Info panel
        self.text_panel = TextPanel()

        # Buttons
        self._btn_swarm = self._build_nav_btn()
        self._btn_home = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _(NavID.FIGARO)

        # Buttons
        self._btn_swarm.text = _(NavID.SWARM)
        self._btn_home.text = _(NavID.HOME)

    # Callback handlers
    def _handel_request(self, _: toga.Widget) -> None:
        self.subject.notify('request_data')

    def _handel_clear(self, _: toga.Widget) -> None:
        self.text_panel.clean()
