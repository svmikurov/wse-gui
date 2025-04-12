"""Defines login page view."""
from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.object_id import ObjectID
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel


class LoginView(BaseView):
    """Login page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.LOGIN

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self.info_panel,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        """Create a user interface."""
        # Page title
        self._label_title = TitleLabel()

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # Navigation buttons
        self._btn_back = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        """Assign a text for UI widgets."""
        # Page title
        self._label_title.text = _(NavigationID.LOGIN)

        # Navigate buttons
        self._btn_back.text = _(NavigationID.BACK)
