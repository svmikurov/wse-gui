"""Home screen the view module."""

import toga

from wse.core.i18n import _
from wse.features.shared.button_names import ButtonName
from wse.features.shared.observer import Subject
from wse.features.text import TitleLabel
from wse.interface.ifeatures import IView
from wse.pages.widgets import BtnApp as AppButton
from wse.pages.widgets import MultilineInfoPanel


class HomeView(IView):
    """View of Home screen."""

    def __init__(self, content: toga.Box) -> None:
        """Construct the view."""
        self.content = content
        self._subject = Subject()

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
        self._btn_login.text = ButtonName.LOGIN
        self._btn_logout.text = ButtonName.LOGOUT
        self._btn_cancel.text = ButtonName.CANCEL
        self._btn_confirm.text = ButtonName.CONFIRM
        # Navigate buttons
        self._btn_foreign.text = ButtonName.FOREIGN_HOME
        self._btn_glossary.text = ButtonName.GLOSSARY_HOME
        self._btn_mathem.text = ButtonName.MATHEM_HOME
        self._btn_exercises.text = ButtonName.EXERCISES_HOME

    # Utility methods
    def _create_nav_btn(self) -> toga.Button:
        return AppButton(on_press=self._notify_navigator)

    def _create_auth_btn(self) -> toga.Button:
        return AppButton(on_press=self._auth_notify)

    @property
    def subject(self) -> Subject:
        """Return the subject (reade-only)."""
        return self._subject

    # Notifications
    def _notify_navigator(self, button: toga.Button) -> None:
        self.subject.notify('navigate', button_text=button.text)

    def _auth_notify(self, button: toga.Button) -> None:
        self.subject.notify('auth', button_text=button.text)
