"""Defines Foreign params page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.boxes import (
    ColumnBox,
)
from wse.features.shared.containers.params import (
    ProgressBox,
    SelectionLabelBox,
    SwitchLabelBox,
    SwitchNumberInputBox,
)
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui.ui_text import TextPanel, TitleLabel


class ParamsView(BaseView):
    """Foreign params view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.FOREIGN_PARAMS

        # Add params UI
        self._create_params_ui()
        self._add_params_ui()
        self._assign_params_ui_text()

        # Add core UI
        self._add_ui()

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
        self.info_panel = TextPanel()

        # NavigationID buttons
        self._btn_goto_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Update all UI elements with current translations."""
        self._label_title.text = _('Foreign params title')
        self._btn_goto_back.text = _(NavigationID.BACK)

    # TODO: Inject params container
    ####################################################################
    # Params widgets

    def _add_params_ui(self) -> None:
        self._params_box = ColumnBox()

        # -= Selections =-
        self._params_box.add(
            self._category_box,
            self._source_box,
            self._order_box,
            self._start_date_box,
            self._end_date_box,
        )

        # -= NumberInputs =-
        self._params_box.add(
            self._input_first_box,
            self._input_last_box,
            self._timeout_box,
        )

        # -= Progress switches =-
        self._params_box.add(self._progress_box)

        # -= Favorites switch =-
        self._params_box.add(self._favorites_box)

    def _create_params_ui(self) -> None:
        # -= Selections =-
        self._category_box = SelectionLabelBox()
        self._source_box = SelectionLabelBox()
        self._order_box = SelectionLabelBox()
        self._start_date_box = SelectionLabelBox()
        self._end_date_box = SelectionLabelBox()

        # -= NumberInputs =-
        self._input_first_box = SwitchNumberInputBox()  # Count of first items
        self._input_last_box = SwitchNumberInputBox()  # Count of last items
        self._timeout_box = SwitchNumberInputBox()

        # -= Progress switches =-
        self._progress_box = ProgressBox()

        # -= Favorites switch =-
        self._favorites_box = SwitchLabelBox()

    def _assign_params_ui_text(self) -> None:
        # -= Selections =-
        self._category_box.text = _('Category')
        self._source_box.text = _('Source')
        self._order_box.text = _('Translate order')
        self._start_date_box.text = _('Period start date')
        self._end_date_box.text = _('Period end date')

        # -= Number inputs =-
        self._input_first_box.text = _('First number count')
        self._input_last_box.text = _('Last number count')
        self._timeout_box.text = _('Timeout')

        # -= Progress switches =-
        self._progress_box.study.text = _('Study')
        self._progress_box.examination.text = _('Examination')
        self._progress_box.repeat.text = _('Repeat')
        self._progress_box.know.text = _('Know')

        # -= Favorites switch =-
        self._favorites_box.text = _('Favorites')
