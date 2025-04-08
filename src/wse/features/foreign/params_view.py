"""Defines Foreign params page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.object_id import ObjectID
from wse.features.shared.base_mvc import BaseView
from wse.features.shared.base_ui import BaseContent, ColumnBox
from wse.features.shared.observer import Subject
from wse.features.shared.params import SelectionBox
from wse.features.shared.text import TitleLabel
from wse.pages.widgets import MultilineInfoPanel


class ParamsView(BaseView):
    """Foreign params view."""

    def __init__(self, content_box: BaseContent | None = None) -> None:
        """Construct the view."""
        super().__init__(content_box)
        self._content.id = ObjectID.FOREIGN_PARAMS

        # Params UI
        self._create_params_ui()
        self._add_params_ui()
        self._assign_params_ui_text()

        # Add UI
        self._create_ui()
        self._add_ui()
        self._assign_ui_text()

    ####################################################################
    # Core widgets

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self.info_panel,
            self._params_box,
            self._category_box,
            self._btn_goto_back,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel('')

        # Info panel
        self.info_panel = MultilineInfoPanel()

        # NavigationID buttons
        self._btn_goto_back = self._create_nav_btn()

    def _assign_ui_text(self) -> None:
        self._label_title.text = _('Foreign params title')
        self._btn_goto_back.text = _(NavigationID.BACK)

    ####################################################################
    # Params widgets

    def _add_params_ui(self) -> None:
        self._params_box = ColumnBox()

        # Fill params box
        self._params_box.add(
            self._category_box,
        )

    def _create_params_ui(self) -> None:
        self._category_box = SelectionBox(Subject())

    def _assign_params_ui_text(self) -> None:
        self._category_box.label.text = _('Category')
