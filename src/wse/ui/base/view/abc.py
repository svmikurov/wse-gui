"""Abstract base class for view."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, override

import toga

from wse.config.layout import StyleConfig, ThemeConfig
from wse.ui.base.container.abc import ContainerGenABC

T_contra = TypeVar('T_contra', contravariant=True)


class NavigableViewABC(
    ABC,
    Generic[T_contra],
):
    """ABC for navigable view."""

    @property
    @abstractmethod
    def content(self) -> toga.Box:
        """Get screen content."""

    @abstractmethod
    def on_open(self, **kwargs: T_contra) -> None:
        """Call methods when screen opens."""

    @abstractmethod
    def on_close(self) -> None:
        """Call methods before close the screen."""


@dataclass
class ViewABC(
    ContainerGenABC[StyleConfig, ThemeConfig],
    ABC,
):
    """Base implementation for page view."""

    _style: StyleConfig
    _theme: ThemeConfig

    # TODO: Make private
    @abstractmethod
    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style.

        See `UpdateStyleABC`.
        """
