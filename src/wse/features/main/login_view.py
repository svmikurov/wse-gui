"""Defines login page view."""

import logging

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.container import BaseContainer
from wse.features.base.mvc import BaseView
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel

logger = logging.getLogger(__name__)


class LoginView(BaseView):
    """Login page view."""

    def __init__(
        self,
        *args: object,
        login_container: BaseContainer | None = None,
        **kwargs: object,
    ) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self.login_container = login_container
        # self.login_container = LoginContainer(content_box=ColumnBox())
        self._content.id = ObjectID.LOGIN

        # Login container

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            *self.login_container.get_content_widgets(),
            self._btn_back,
            self.info_panel,
        )

    def _create_ui(self) -> None:
        """Create a user interface."""
        # Page title
        self._label_title = TitleLabel()

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # Navigation buttons
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign a text for UI widgets."""
        # Page title
        self._label_title.text = _(NavigationID.LOGIN)

        # Navigate buttons
        self._btn_back.text = _(NavigationID.BACK)
