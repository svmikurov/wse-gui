"""Defines account page view."""

import toga

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.button import AppButton
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_text import TextPanel, TitleLabel


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
            self._btn_check_token,
            self._btn_clean_panel,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        self._label_title = TitleLabel()
        self.info_panel = TextPanel()
        self._btn_auth = self._build_nav_btn()
        self._btn_check_token = AppButton(on_press=self._check_token)
        self._btn_clean_panel = AppButton(on_press=self._clean_panel)
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign to widget text a current translation."""
        self._label_title.text = _(NavigationID.ACCOUNT)
        self._btn_auth.text = _(NavigationID.LOGOUT)
        self._btn_check_token.text = _('Check token')
        self._btn_clean_panel.text = _('Clean panel')
        self._btn_back.text = _(NavigationID.BACK)

    def update_auth_button(self, nav_id: NavigationID) -> None:
        """Assign to auth button a value by status and translation."""
        self._btn_auth.text = _(nav_id)

    ####################################################################
    # Callback handlers
    def _check_token(self, _: toga.Button) -> None:
        self.subject.notify('check_token')

    def _clean_panel(self, _: toga.Button) -> None:
        self.subject.notify('clean_panel')
