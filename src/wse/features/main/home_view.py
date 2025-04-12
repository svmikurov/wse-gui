"""Home screen the view module."""

import toga

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import NavigableView
from wse.features.shared.action_id import ActionID
from wse.features.shared.button import AppButton
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel


class HomeView(NavigableView):
    """View of Home screen."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.HOME

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
            self._label_title,
            self.info_panel,
            self._btn_account,
            self._btn_foreign,
            self._btn_glossary,
            self._btn_mathem,
            self._btn_exercises,
        )

    def _build_ui(self) -> None:
        # Title
        self._label_title = TitleLabel()

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # Auth buttons
        self._btn_login = self._build_nav_btn()
        self._btn_logout = self._build_auth_btn()
        self._btn_cancel = self._build_auth_btn()
        self._btn_confirm = self._build_auth_btn()

        # Navigate buttons
        self._btn_account = self._build_nav_btn()
        self._btn_foreign = self._build_nav_btn()
        self._btn_glossary = self._build_nav_btn()
        self._btn_mathem = self._build_nav_btn()
        self._btn_exercises = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign to widget text a current translation."""
        self._label_title.text = _('WSELFEDU')

        # Auth buttons
        self._btn_account.text = _(NavigationID.ACCOUNT)
        self._btn_login.text = _(NavigationID.LOGIN)
        self._btn_logout.text = _(NavigationID.LOGOUT)
        self._btn_cancel.text = _(ActionID.CANCEL)
        self._btn_confirm.text = _(ActionID.CONFIRM)

        # Navigate buttons
        self._btn_foreign.text = _(NavigationID.FOREIGN)
        self._btn_glossary.text = _(NavigationID.GLOSSARY)
        self._btn_mathem.text = _(NavigationID.MATHEM)
        self._btn_exercises.text = _(NavigationID.EXERCISES)

    # Utility methods
    def _build_auth_btn(self) -> toga.Button:
        return AppButton(on_press=self._auth_notify)

    # Notifications
    def _auth_notify(self, button: toga.Button) -> None:
        self.subject.notify('auth', nav_id=button.text)
