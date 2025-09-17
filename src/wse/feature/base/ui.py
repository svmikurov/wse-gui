"""Abstract base classes for UI layer."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig

from .abstract.ui_layer import ContentABC
from .container import ContainerABC
from .mixins import SetupMixin

# View


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


# Controller


@dataclass
class Controller(
    SetupMixin,
    ContentABC,
    ABC,
):
    """Abstract base class for controller."""
