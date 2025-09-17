"""Abstract base classes."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.navigation.nav_id import NavID
from wse.feature.base.container import ContainerABC


class NavigateABC(ABC):
    """ABC for navigate feature."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event."""


class CloseScreenABC(ABC):
    """ABC for close screen event."""

    @abstractmethod
    def on_close(self) -> None:
        """Call methods before close the screen."""


@dataclass
class ViewABC(
    ContainerABC[StyleConfig, ThemeConfig],
    ABC,
):
    """Base implementation for page view."""

    _style: StyleConfig
    _theme: ThemeConfig

    @abstractmethod
    @override
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style.

        See `UpdateStyleABC`.
        """
