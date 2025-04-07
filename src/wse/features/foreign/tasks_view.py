"""Foreign tasks page view."""

from wse.core.i18n import _
from wse.core.navigaion.navigation_id import NavigationID
from wse.features.object_id import ObjectID
from wse.features.shared.base import BaseView
from wse.features.shared.base_ui import BaseContent
from wse.features.text import TitleLabel
from wse.pages.widgets import MultilineInfoPanel


class TasksView(BaseView):
    """Foreign tasks view."""

    def __init__(self, content_box: BaseContent | None = None) -> None:
        """Construct the view."""
        super().__init__(content_box)
        self._content.id = ObjectID.FOREIGN_TASKS

        # Add UI
        self._create_ui()
        self._assign_ui_text()
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
            self._label_title,
            self.info_panel,
            self._btn_goto_test,
            self._btn_goto_back,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel('')

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # NavigationID buttons
        self._btn_goto_test = self._create_nav_btn()
        self._btn_goto_back = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        # Title
        self._label_title.text = _('Foreign tasks title')

        # NavigationID buttons
        self._btn_goto_test.text = NavigationID.FOREIGN_TESTS
        self._btn_goto_back.text = NavigationID.BACK
