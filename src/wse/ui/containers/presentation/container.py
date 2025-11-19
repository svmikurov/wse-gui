"""Presentation exercise container."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer.accessor import AccessorMixin
from wse.ui.base.content.mixins import GetContentMixin

from . import PresentationContainerABC


@inject
@dataclass
class PresentationContainer(
    GetContentMixin,
    AccessorMixin,
    PresentationContainerABC,
):
    """Presentation exercise container."""

    _accessors = 'definition', 'explanation'

    @override
    def _create_ui(self) -> None:
        style = self._style.presenter

        self._definition = toga.Label('')
        self._explanation = toga.Label('')

        self._definition_scroll = toga.ScrollContainer(
            content=self._definition,
            height=style.definition.get('height'),
        )
        self._explanation_scroll = toga.ScrollContainer(
            content=self._explanation,
            height=style.explanation.get('height'),
        )

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._definition_scroll,
            self._explanation_scroll,
        )

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._definition.style.update(**config.presenter.definition)
        self._explanation.style.update(**config.presenter.explanation)

    @override
    def change(self, accessor: str, value: object) -> None:
        """Change ui context via accessor."""
        self._get_ui(accessor).text = value
