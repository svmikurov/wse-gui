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

    _accessors = 'question', 'answer'

    @override
    def _create_ui(self) -> None:
        style = self._style.presenter

        self._question = toga.Label('')
        self._answer = toga.Label('')

        self._question_scroll = toga.ScrollContainer(
            content=self._question,
            height=style.question.get('height'),
        )
        self._answer_scroll = toga.ScrollContainer(
            content=self._answer,
            height=style.answer.get('height'),
        )

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._question_scroll,
            self._answer_scroll,
        )

    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        self._question.style.update(**config.presenter.question)
        self._answer.style.update(**config.presenter.answer)

    @override
    def change(self, accessor: str, value: object) -> None:
        """Change ui context via accessor."""
        self._get_ui(accessor).text = value
