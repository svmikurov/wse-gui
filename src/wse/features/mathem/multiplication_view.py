"""Defines Multiplication page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.boxes import ColumnFlexBox
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui.ui_text import TitleLabel
from wse.interface.imathem import INumericKeypad


class MultiplicationView(BaseView):
    """Multiplication page view."""

    def __init__(
        self,
        *args: object,
        numeric_keypad: INumericKeypad,
        **kwargs: object,
    ) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._numeric_keypad = numeric_keypad
        self._content.id = ObjectID.MULTIPLICATION

        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            ColumnFlexBox(),
            self._numeric_keypad.keypad_v1,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        """Build a user interface."""
        self._label_title = TitleLabel()
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _('Multiplication title')
        self._btn_back.text = _(NavigationID.BACK)
