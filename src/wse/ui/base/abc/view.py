"""Abstract base classe for view."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.ui.base.abc.container import ContainerABC


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
