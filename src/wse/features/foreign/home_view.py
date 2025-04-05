"""Foreign home page view."""

import toga

from wse.core.i18n import _
from wse.features.obj_test_id import ObjectTestID
from wse.features.shared.base import BaseContent
from wse.features.shared.button_text import ButtonText
from wse.features.shared.observer import Subject
from wse.features.text import TitleLabel
from wse.interface.ifeatures import IView
from wse.pages.widgets import AppButton, MultilineInfoPanel


class ForeignView(IView):
    """Foreign home page view."""

    def __init__(self, content: BaseContent | None = None) -> None:
        """Construct the page."""
        super().__init__()
        # Page content
        self._content = content or toga.Box()
        self._content.test_id = ObjectTestID.FOREIGN_VIEW

        # Listeners
        self._subject = Subject()

        # Add UI
        self._create_ui()
        self._assign_ui_text()
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
            self._label_title,
            self.info_panel,
            self._btn_goto_tasks,
            self._btn_goto_params,
            self._btn_goto_create,
            self._btn_goto_back,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel('')

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # Navigation buttons
        self._btn_goto_tasks = self._create_nav_btn()
        self._btn_goto_params = self._create_nav_btn()
        self._btn_goto_create = self._create_nav_btn()
        self._btn_goto_back = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        # Title
        self._label_title.text = _('Foreign title')

        # Navigation buttons
        self._btn_goto_tasks.text = ButtonText.FOREIGN_TASKS
        self._btn_goto_params.text = ButtonText.FOREIGN_PARAMS
        self._btn_goto_create.text = ButtonText.FOREIGN_CREATE
        self._btn_goto_back.text = ButtonText.BACK

    # Utility methods
    def _create_nav_btn(self) -> toga.Button:
        return AppButton(on_press=self._notify_navigator)

    @property
    def subject(self) -> Subject:
        """Return the subject (read-only)."""
        return self._subject

    @property
    def title(self) -> str:
        """Page title (read-only)."""
        return self._label_title.text

    @property
    def content(self) -> BaseContent:
        """Page content (read-only)."""
        return self._content

    # Notifications
    def _notify_navigator(self, button: toga.Button) -> None:
        self.subject.notify('navigate', button_text=button.text)
