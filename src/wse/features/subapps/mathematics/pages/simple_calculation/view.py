"""Defines Simple math calculation page view."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base import BaseView
from wse.features.subapps.nav_id import NavID
from wse.utils.i18n import label_, nav_


@inject
@dataclass
class SimpleCalcView(BaseView):
    """Simple math calculation page view."""

    def _setup(self) -> None:
        self._content.test_id = NavID.SIMPLE_CALC

    def _populate_content(self) -> None:
        self.content.add(
            self._label_title,
            self._btn_back,
        )

    def _create_ui(self) -> None:
        self._label_title = toga.Label('')
        self._btn_back = self._create_nav_btn(nav_id=NavID.BACK)

    # TODO: Implement a style update
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._label_title.style.update(**config.title)
        self._btn_back.style.update(**config.btn_nav)

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._label_title.text = label_('Simple calculation title')
        self._btn_back.text = nav_(NavID.BACK)
