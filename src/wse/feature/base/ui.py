"""Abstract base classes for UI layer."""

from abc import ABC
from dataclasses import dataclass

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


# Controller


@dataclass
class Controller(
    SetupMixin,
    ContentABC,
    ABC,
):
    """Abstract base class for controller."""
