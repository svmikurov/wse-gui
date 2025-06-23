"""Defines Main Mathematical application page view."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import label_, nav_


@inject
@dataclass
class IndexMathView(BaseView):
    """Main Mathematical application page view."""

    def __post_init__(self) -> None:
        """Construct the page."""
        super().__post_init__()
        self._content.test_id = NavID.INDEX_MATH

    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._btn_nav_home,
        )

    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_nav_home = self._create_nav_btn(nav_id=NavID.HOME)

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.title)
        self._btn_nav_home.style.update(**config.btn_nav)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Mathematical page title')
        self._btn_nav_home.text = nav_(NavID.HOME)
