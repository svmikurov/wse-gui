"""Defines Swarm page view."""

import logging

import toga

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.figaro.containers.swarm_panel import SwarmControlPanel
from wse.features.shared.button import AppButton
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_text import AppTextPanel, TitleLabel

logger = logging.getLogger(__name__)


class SwarmView(BaseView):
    """Swarm page view."""

    def __init__(
        self,
        *args: object,
        swarm_panel: SwarmControlPanel | None = None,
        **kwargs: object,
    ) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._swarm_panel = swarm_panel
        self._content.id = ObjectID.SWARM

        # Construct UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            *self._swarm_panel.get_content_widgets(),
            self.text_panel,
            self._btn_request,
            self._btn_clear,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel()

        # Info panel
        self.text_panel = AppTextPanel()

        # Buttons
        self._btn_request = AppButton(on_press=self._handel_request)
        self._btn_clear = AppButton(on_press=self._handel_clear)
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _(NavigationID.SWARM)

        # Buttons
        self._btn_request.text = _('Request')
        self._btn_clear.text = _('Clear')
        self._btn_back.text = _(NavigationID.BACK)

    # Callback handlers
    def _handel_request(self, _: toga.Widget) -> None:
        self.subject.notify('handel_request', endpoint=self._get_url())

    def _handel_clear(self, _: toga.Widget) -> None:
        self.text_panel.clean()

    def _get_url(self) -> str:
        endpoint = self._swarm_panel.data['endpoint']
        return endpoint
