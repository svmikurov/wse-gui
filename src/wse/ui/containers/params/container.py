"""Params container."""

from dataclasses import dataclass
from typing import Any, override

import toga
from injector import inject

from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.content.mixins import GetContentMixin

from . import ParamsContainerABC, ParamsContainerModelABC


@inject
@dataclass
class ParamsContainerModel(
    ObserverManagerGen[Any],
    ParamsContainerModelABC,
):
    """Params container model."""


@inject
@dataclass
class ParamsContainer(
    GetContentMixin,
    ParamsContainerABC,
):
    """Params container."""

    @override
    def _create_ui(self) -> None:
        self._word_count_select = toga.Selection()

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._word_count_select,
        )
