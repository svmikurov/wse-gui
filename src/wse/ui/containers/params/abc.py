"""Abstract base classes for Params container."""

from abc import ABC
from dataclasses import dataclass
from typing import Any

from wse.feature.observer.abc import (
    AccessorABC,
    AccessorNotifyChangeABC,
)
from wse.feature.observer.generic import (
    ObserverManagerGenABC,
)
from wse.ui.base.container import ContainerABC
from wse.ui.base.content import ContentABC, GetContentABC


@dataclass
class ParamsContainerABC(
    AccessorABC,
    AccessorNotifyChangeABC,
    ObserverManagerGenABC[Any],
    GetContentABC,
    ContainerABC,
    ABC,
):
    """ABC for Params container."""

    _content: ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._check_accessors()
