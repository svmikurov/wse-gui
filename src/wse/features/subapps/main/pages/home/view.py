"""Home page view of ain feature."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import label_, nav_


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
        self._btn_math = self._create_nav_btn(nav_id=NavID.INDEX_MATH)

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.title)
        self._btn_math.style.update(**config.btn_nav)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Home page title')
        self._btn_math.text = nav_(NavID.INDEX_MATH)
