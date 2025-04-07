"""Home screen the view module."""

import toga

from wse.core.i18n import _
from wse.core.navigaion.navigation_id import NavigationID
from wse.features.object_id import ObjectID
from wse.features.shared.base import BaseView
from wse.features.shared.base_ui import BaseContent
from wse.features.text import TitleLabel
from wse.pages.widgets import BtnApp as AppButton
from wse.pages.widgets import MultilineInfoPanel


class HomeView(BaseView):
    """View of Home screen."""

    def __init__(self, content_box: BaseContent | None = None) -> None:
        """Construct the view."""
        super().__init__(content_box)
        self._content.id = ObjectID.HOME

        # Add UI
        self._create_ui()
        self._assign_ui_text()
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
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
        self._btn_login.text = _(NavigationID.LOGIN)
        self._btn_logout.text = _(NavigationID.LOGOUT)
        self._btn_cancel.text = _(NavigationID.CANCEL)
        self._btn_confirm.text = _(NavigationID.CONFIRM)

        # Navigate buttons
        self._btn_foreign.text = _(NavigationID.FOREIGN)
        self._btn_glossary.text = _(NavigationID.GLOSSARY)
        self._btn_mathem.text = _(NavigationID.MATHEM)
        self._btn_exercises.text = _(NavigationID.EXERCISES)

    # Utility methods
    def _create_auth_btn(self) -> toga.Button:
        return AppButton(on_press=self._auth_notify)

    # Notifications
    def _auth_notify(self, button: toga.Button) -> None:
        self.subject.notify('auth', navigation_id=button.text)
