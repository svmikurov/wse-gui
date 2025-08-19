"""Defines Exercise completion page view."""

from dataclasses import dataclass

import toga
from injector import inject

from wse.apps.nav_id import NavID
from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.shared.containers.top_bar import TopBarPageViewMixin
from wse.utils.i18n import nav_

from .iabc import ExerciseViewABC


@inject
@dataclass
class ExerciseView(
    TopBarPageViewMixin,
    ExerciseViewABC,
):
    """Exercise completion page view."""

    def _create_ui(self) -> None:
        self._title = toga.Label('')

    def _populate_content(self) -> None:
        self.content.add(
            self._top_bar.content,
            self._title,
        )

    def localize_ui(self) -> None:
        """Localize the UI text."""
        self._title.text = nav_(NavID.EXERCISE)

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._title.style.update(**config.label_title)
