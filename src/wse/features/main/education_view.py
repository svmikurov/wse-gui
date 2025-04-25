"""Defines Education page view."""

from wse.core.i18n import _
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.mvc import BaseView
from wse.features.shared.object_id import ObjectID
from wse.features.shared.ui_text import TextPanel, TitleLabel


class EducationView(BaseView):
    """Education page view."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the view."""
        super().__init__(*args, **kwargs)
        self._content.id = ObjectID.EDUCATION

        # Add UI
        self._add_ui()

    def _add_ui(self) -> None:
        self._content.add(
            self._label_title,
            self.info_panel,
            self._btn_account,
            self._btn_foreign,
            self._btn_glossary,
            self._btn_mathem,
            self._btn_exercises,
            self._btn_home,
        )

    def _create_ui(self) -> None:
        # Title
        self._label_title = TitleLabel()

        # Info panel
        self.info_panel = TextPanel()

        # Navigate buttons
        self._btn_account = self._build_nav_btn()
        self._btn_foreign = self._build_nav_btn()
        self._btn_glossary = self._build_nav_btn()
        self._btn_mathem = self._build_nav_btn()
        self._btn_exercises = self._build_nav_btn()
        self._btn_home = self._build_nav_btn()

    def localize_ui(self) -> None:
        """Assign to widget text a current translation."""
        self._label_title.text = _('WSELFEDU')

        # Navigate buttons
        self._btn_account.text = _(NavigationID.ACCOUNT)
        self._btn_foreign.text = _(NavigationID.FOREIGN)
        self._btn_glossary.text = _(NavigationID.GLOSSARY)
        self._btn_mathem.text = _(NavigationID.MATHEMATICAL)
        self._btn_exercises.text = _(NavigationID.EXERCISES)
        self._btn_home.text = _(NavigationID.HOME)
