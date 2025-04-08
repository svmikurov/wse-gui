"""Foreign home page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.object_id import ObjectID
from wse.features.shared.mvc import BaseView
from wse.features.shared.ui_containers import BaseContent
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel


class ForeignView(BaseView):
    """Foreign home page view."""

    def __init__(self, content_box: BaseContent | None = None) -> None:
        """Construct the page."""
        super().__init__(content_box)
        self._content.id = ObjectID.FOREIGN

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

        # NavigationID buttons
        self._btn_goto_tasks = self._create_nav_btn()
        self._btn_goto_params = self._create_nav_btn()
        self._btn_goto_create = self._create_nav_btn()
        self._btn_goto_back = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        # Title
        self._label_title.text = _('Foreign title')

        # NavigationID buttons
        self._btn_goto_tasks.text = _(NavigationID.FOREIGN_TASKS)
        self._btn_goto_params.text = _(NavigationID.FOREIGN_PARAMS)
        self._btn_goto_create.text = _(NavigationID.FOREIGN_CREATE)
        self._btn_goto_back.text = _(NavigationID.BACK)
