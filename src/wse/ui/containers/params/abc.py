"""Abstract base classes for Params container."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal, TypeAlias

from wse.data.dto import foreign as dto
from wse.feature import observer
from wse.feature.observer import generic
from wse.ui.base import container, content

NotifyT: TypeAlias = Literal['update']


@dataclass
class ParamsContainerABC(
    observer.AccessorABC,
    observer.UpdateObserverABC[dto.OptionAccessor],
    generic.ObserverManagerGenABC[Any],
    content.GetContentABC,
    container.ContainerABC,
    container.StyleABC,
    ABC,
):
    """ABC for Params container."""

    _content: content.ContentABC

    def __post_init__(self) -> None:
        """Construct the container."""
        self._create_ui()
        self._populate_content()
        self._check_accessors()
        self._apply_styles()

    @abstractmethod
    def set_values(self, accessor: dto.OptionAccessor, values: object) -> None:
        """Set widget values via accessor.

        Updated widget must implement ``items.update()`` Source
        interface.
        """

    @abstractmethod
    def set_value(
        self,
        accessor: dto.ParameterAccessors,
        value: object,
    ) -> None:
        """Set widget value via accessor."""
