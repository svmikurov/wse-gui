"""Defines Mathematical page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui.ui_text import TextPanel, TitleLabel


class MathematicalView(BaseView):
    """Mathematical page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.MATHEMATICAL

        self._add_ui()

    def _add_ui(self) -> None:
        self.content.add(
            self._label_title,
            self.text_panel,
            self._btn_multiplication,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        """Build a user interface."""
        self._label_title = TitleLabel()
        self.text_panel = TextPanel()
        self._btn_multiplication = self._build_nav_btn()
        self._btn_back = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Localize a text for user interface widgets."""
        self._label_title.text = _('Mathematical title')
        self._btn_multiplication.text = _(NavigationID.MULTIPLICATION)
        self._btn_back.text = _(NavigationID.BACK)
