"""Info container."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer.accessor import AccessorMixin
from wse.ui.base.content.mixins import GetContentMixin

from .abc import InfoContainerABC


@inject
@dataclass
class InfoContainer(
    GetContentMixin,
    AccessorMixin,
    InfoContainerABC,
):
    """Info container."""

    _accessors = ('progress',)

    @override
    def _populate_content(self) -> None:
        self.content.add(
            self._progress,
        )

    @override
    def _create_ui(self) -> None:
        self._progress = toga.Label('')

    @override
    def _update_style(self, config: StyleConfig | ThemeConfig) -> None:
        self._progress.style.update(**config.info.label)

    @override
    def change(self, accessor: str, value: object) -> None:
        """Change ui context via accessor."""
        self._get_ui(accessor).text = value
