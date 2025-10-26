"""Abstract base classes for Params container."""

from abc import ABC
from dataclasses import dataclass
from typing import Any

from wse.feature.observer.generic import (
    ObserverManagerGenABC,
)
from wse.ui.base.container import ContainerABC
from wse.ui.base.content import ContentABC, GetContentABC


class ParamsContainerModelABC(
    ObserverManagerGenABC[Any],
    ABC,
):
    """ABC for Params container model."""


@dataclass
class ParamsContainerABC(
    GetContentABC,
    ContainerABC,
    ABC,
):
    """ABC for Params container."""

    _content: ContentABC
    _state: ParamsContainerModelABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._state.add_observer(self)
        self._create_ui()
        self._populate_content()
