"""Presenter container."""

from dataclasses import dataclass
from typing import override

import toga
from injector import inject

from wse.ui.base.content.mixins import GetContentMixin

from . import AccessorMixin, LabelAccessorContainerABC


@inject
@dataclass
class PresenterContainer(
    GetContentMixin,
    AccessorMixin,
    LabelAccessorContainerABC,
):
    """Presenter container."""

    _accessors: list[str] = ['definition', 'explanation']

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

    # Lister methods

    @override
    def change(self, accessor: str, value: str) -> None:
        """Change ui context via accessor."""
        self._get_ui(accessor).text = value
