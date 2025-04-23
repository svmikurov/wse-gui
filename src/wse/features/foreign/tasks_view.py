"""Foreign tasks page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_containers import BaseContent
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel


class TasksView(BaseView):
    """Foreign tasks view."""

    def __init__(self, content_box: BaseContent | None = None) -> None:
        """Construct the view."""
        super().__init__(content_box)
        self._content.id = ObjectID.FOREIGN_TASKS

        # Add UI
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
        self._btn_goto_test = self._build_nav_btn()
        self._btn_goto_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Update all UI elements with current translations."""
        # Title
        self._label_title.text = _('Foreign tasks title')

        # NavigationID buttons
        self._btn_goto_test.text = _(NavigationID.FOREIGN_TESTS)
        self._btn_goto_back.text = _(NavigationID.BACK)
