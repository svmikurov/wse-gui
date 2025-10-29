"""Abstract base class for label listener container via accessors."""

from abc import ABC
from dataclasses import dataclass
from typing import Any

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer import AccessorABC, ChangeObserverABC
from wse.ui.base.container.abc import ApplyStyleGenABC, ContainerABC
from wse.ui.base.content.abc import GetContentABC


@dataclass
class LabelAccessorContainerABC(
    ContainerABC,
    AccessorABC,
    ChangeObserverABC[Any],  # TODO: Fix Any
    GetContentABC,
    ApplyStyleGenABC[StyleConfig, ThemeConfig],
    ABC,
):
    """ABC for label listener container via accessors."""

    _style: StyleConfig
    _theme: ThemeConfig

    def __post_init__(self) -> None:
        """Construct the accessor."""
        self._create_ui()
        self._populate_content()
        self._check_accessors()
        self._apply_styles()

    def _apply_styles(self) -> None:
        self.update_style(self._style)
        self.update_style(self._theme)
