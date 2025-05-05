"""Defines Home page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavID
from wse.features.base.mvc import BaseView
from wse.features.shared.enums.object_id import ObjectID
from wse.features.shared.ui.ui_text import TextPanel, TitleLabel


class HomeView(BaseView):
    """Home page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.HOME

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
            self._label_title,
            self.info_panel,
            self._btn_account,
            self._btn_education,
            self._btn_examples,
            self._btn_figaro,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel()

        # Info panel
        self.info_panel = TextPanel()

        # Navigate buttons
        self._btn_account = self._build_nav_btn()
        self._btn_education = self._build_nav_btn()
        self._btn_examples = self._build_nav_btn()
        self._btn_figaro = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign to widget text a current translation."""
        self._label_title.text = _('WSELFEDU')

        # Navigate buttons
        self._btn_account.text = _(NavID.ACCOUNT)
        self._btn_education.text = _(NavID.EDUCATION)
        self._btn_examples.text = _(NavID.EXAMPLES)
        self._btn_figaro.text = _(NavID.FIGARO)
