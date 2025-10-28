"""Abstract base classes for Params container."""

from abc import ABC
from dataclasses import dataclass
from typing import Any, Literal

from wse.core.base.enums import BaseEnum
from wse.feature.observer import (
    AccessorABC,
    UpdateObserverABC,
)
from wse.feature.observer.generic import (
    ObserverManagerGenABC,
)
from wse.ui.base.container import ContainerABC, StyleABC
from wse.ui.base.content import ContentABC, GetContentABC

ParamsNotifyT = Literal['update']


class ParamsAccessorEnum(BaseEnum):
    """Params accessor enumeration."""

    MARK_SELECT = 'mark_select'
    CATEGORY_SELECT = 'category_select'
    COUNT_INPUT = 'count_input'


@dataclass
class ParamsContainerABC(
    AccessorABC,
    UpdateObserverABC[ParamsAccessorEnum],
    ObserverManagerGenABC[Any],
    GetContentABC,
    ContainerABC,
    StyleABC,
    ABC,
):
    """ABC for Params container."""

    _content: ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._check_accessors()
        self._apply_styles()
