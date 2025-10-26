"""Presenter container."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer.accessor import AccessorMixin
from wse.ui.base.content.mixins import GetContentMixin

from . import LabelAccessorContainerABC


@inject
@dataclass
class PresenterContainer(
    GetContentMixin,
    AccessorMixin,
    LabelAccessorContainerABC,
):
    """Presenter container."""

    def __post_init__(self) -> None:
        """Construct the container."""
        self._accessors: tuple[str, ...] = 'definition', 'explanation'
        super().__post_init__()

    # Building the container

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

    # Lister methods

    @override
    def change(self, accessor: str, value: str) -> None:
        """Change ui context via accessor."""
        self._get_ui(accessor).text = value
