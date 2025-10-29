"""Presenter container."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer.accessor import AccessorMixin
from wse.ui.base.content.mixins import GetContentMixin

from . import PresenterContainerABC


@inject
@dataclass
class PresenterContainer(
    GetContentMixin,
    AccessorMixin,
    PresenterContainerABC,
):
    """Presenter container."""

    _accessors = 'definition', 'explanation'

    @override
    def _create_ui(self) -> None:
        self._definition = toga.Label('')
        self._explanation = toga.Label('')

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._definition,
            self._explanation,
        )

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._definition.style.update(**config.presenter.definition)
        self._explanation.style.update(**config.presenter.explanation)

    # Source methods
    # --------------

    @override
    def change(self, accessor: str, value: object) -> None:
        """Change ui context via accessor."""
        self._get_ui(accessor).text = value
