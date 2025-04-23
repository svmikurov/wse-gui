"""Defines account page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel


class AccountView(BaseView):
    """Account page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.ACCOUNT

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
            self._label_title,
            self.info_panel,
            self._btn_auth,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        self._label_title = TitleLabel()
        self.info_panel = MultilineInfoPanel()
        self._btn_auth = self._build_nav_btn()
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign to widget text a current translation."""
        self._label_title.text = _(NavigationID.ACCOUNT)
        self._btn_back.text = _(NavigationID.BACK)
        self._btn_auth.text = _(NavigationID.LOGOUT)

    def update_auth_button(self, nav_id: NavigationID) -> None:
        """Assign to auth button a value by status and translation."""
        self._btn_auth.text = _(nav_id)
