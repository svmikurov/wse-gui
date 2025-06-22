"""Home page view of ain feature."""

from dataclasses import dataclass

import toga
from injector import inject
from toga.style import Pack

from wse.features.apps.nav_id import NavID
from wse.features.base import BaseView
from wse.utils.i18n import _


@inject
@dataclass
class HomeView(BaseView):
    """Home page view of main feature."""

    def __post_init__(self) -> None:
        """Construct the page."""
        super().__post_init__()
        self._content.test_id = NavID.HOME

    def _populate_content(self) -> None:
        self._content.add(
            self._label_title,
            self._btn_math,
        )

    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_math = self._create_nav_btn()

    def update_style(self) -> None:
        """Update widgets style."""
        self._label_title.style = Pack(**self._config.title)
        self._btn_math.style = Pack(**self._config.btn_nav)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = _('Home page')
        self._btn_math.text = _(NavID.INDEX_MATH)
