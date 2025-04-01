"""Home screen the view module."""

import toga

from wse.core.i18n import _
from wse.core.navigaion.routes import Routes
from wse.features.shared.observer import Subject
from wse.features.text import TitleLabel
from wse.pages.widgets import MultilineInfoPanel
from wse.pages.widgets import BtnApp as AppButton


class HomeView:
    """View of Home screen."""

    def __init__(self, screen: toga.Box | None = None) -> None:
        """Construct the view."""
        self.content = screen or toga.Box()
        self.subject = Subject()

        self._create_ui()
        self._assign_ui_text()
        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self.info_panel,
            self._btn_foreign,
            self._btn_glossary,
            self._btn_mathem,
            self._btn_exercises,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel('')
        # Info panel
        self.info_panel = MultilineInfoPanel()
        # Auth buttons
        self._btn_login = self._create_nav_btn()
        self._btn_logout = self._create_auth_btn()
        self._btn_cancel = self._create_auth_btn()
        self._btn_confirm = self._create_auth_btn()
        # Navigate buttons
        self._btn_foreign = self._create_nav_btn()
        self._btn_glossary = self._create_nav_btn()
        self._btn_mathem = self._create_nav_btn()
        self._btn_exercises = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        """Assign to widget text a current translation."""
        self._label_title.text = _('WSELFEDU')
        # Auth buttons
        self._btn_login.text = Routes.LOGIN.btn_text
        self._btn_logout.text = _('Logout')
        self._btn_cancel.text = _('Cancel')
        self._btn_confirm.text = _('Confirm')
        # Navigate buttons
        self._btn_foreign.text = Routes.FOREIGN_HOME.btn_text
        self._btn_glossary.text = Routes.GLOSSARY_HOME.btn_text
        self._btn_mathem.text = Routes.MATHEM_HOME.btn_text
        self._btn_exercises.text = Routes.EXERCISES_HOME.btn_text

    # Utility methods
    def _create_nav_btn(self) -> toga.Button:
        return AppButton(on_press=self._notify_navigator)

    def _create_auth_btn(self) -> toga.Button:
        return AppButton(on_press=self._auth_notify)

    # Notifications
    def _notify_navigator(self, btn: toga.Button) -> None:
        self.subject.notify('navigate', btn_text=btn.text)

    def _auth_notify(self, btn: toga.Button) -> None:
        self.subject.notify('auth', btn_text=btn.text)
