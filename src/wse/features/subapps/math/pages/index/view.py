"""Defines Main Math page view."""

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
    """Main Math page view."""

    def _setup(self) -> None:
        self._content.test_id = NavID.INDEX_MATH

    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._btn_nav_simple,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_nav_simple = self._create_nav_btn(nav_id=NavID.SIMPLE_CALC)
        self._btn_back = self._create_nav_btn(nav_id=NavID.BACK)

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.label_title)
        self._btn_back.style.update(**config.btn_nav)
        self._btn_nav_simple.style.update(**config.btn_nav)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Main math page title')
        self._btn_nav_simple.text = nav_(NavID.SIMPLE_CALC)
        self._btn_back.text = nav_(NavID.BACK)
