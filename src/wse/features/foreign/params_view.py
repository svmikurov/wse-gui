"""Defines Foreign params page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.object_id import ObjectID
from wse.features.shared.mvc import BaseView
from wse.features.shared.ui_containers import BaseContent, ColumnBox
from wse.features.shared.ui_params import SelectionBox, SwitchNumberInputBox
from wse.features.shared.ui_text import MultilineInfoPanel, TitleLabel


class ParamsView(BaseView):
    """Foreign params view."""

    def __init__(self, content_box: BaseContent | None = None) -> None:
        """Construct the view."""
        super().__init__(content_box)
        self._content.id = ObjectID.FOREIGN_PARAMS

        # Add params UI
        self._create_params_ui()
        self._add_params_ui()
        self._assign_params_ui_text()

        # Add core UI
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
            # -= Selections =-
            self._category_box,
            self._source_box,
            self._order_box,
            self._start_date_box,
            self._end_date_box,
            # -= NumberInputs =-
            self._input_first_box,
            self._input_last_box,
            self._timeout_box,
        )

    def _create_params_ui(self) -> None:
        # -= Selections =-
        self._category_box = SelectionBox()
        self._source_box = SelectionBox()
        self._order_box = SelectionBox()
        self._start_date_box = SelectionBox()
        self._end_date_box = SelectionBox()

        # -= NumberInputs =-
        # Count of first items
        self._input_first_box = SwitchNumberInputBox()
        # Count of last items
        self._input_last_box = SwitchNumberInputBox()
        self._timeout_box = SwitchNumberInputBox()

    def _assign_params_ui_text(self) -> None:
        # -= Selections =-
        self._category_box.label.text = _('Category')
        self._source_box.label.text = _('Source')
        self._order_box.label.text = _('Translate order')
        self._start_date_box.label.text = _('Period start date')
        self._end_date_box.label.text = _('Period end date')

        # -= NumberInputs =-
        self._input_first_box.label.text = _('First number count')
        self._input_last_box.label.text = _('Last number count')
        self._timeout_box.label.text = _('Timeout')
