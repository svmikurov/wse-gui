"""Defines Practice page view."""

import toga
from toga.style import Pack

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.enums.object_id import ObjectID
from wse.features.shared.ui.button import AppButton
from wse.features.shared.ui.ui_text import TextPanel, TitleLabel


class PracticeView(BaseView):
    """Practice page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.PRACTICE

        # Construct UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self._label,
            self.text_panel,
            self._btn_request,
            self._btn_clear,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel()

        # Info panel
        self.text_panel = TextPanel()
        self._label = toga.Label(
            'Experiments with dictionary representation',
            style=Pack(flex=1, padding=(0, 0, 10, 10)),
        )

        # Buttons
        self._btn_request = AppButton(on_press=self._handel_request)
        self._btn_clear = AppButton(on_press=self._handel_clear)
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _(NavigationID.PRACTICE)

        # Buttons
        self._btn_request.text = _('Request text')
        self._btn_clear.text = _('Clear text')
        self._btn_back.text = _(NavigationID.BACK)

    # Callback handlers
    def _handel_request(self, _: toga.Widget) -> None:
        self.subject.notify('request_data')

    def _handel_clear(self, _: toga.Widget) -> None:
        self.text_panel.clean()
