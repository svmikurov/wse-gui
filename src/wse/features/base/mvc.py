"""Defines base class for MVC model components."""

import logging
from abc import ABC
from dataclasses import dataclass

from injector import inject
from typing_extensions import override

from wse.core.interfaces import INavigator

from ...config.layout import StyleConfig, ThemeConfig
from ..interfaces.icontent import IContent
from ..interfaces.imvc import IView
from ._abc.mvc import ContentABC
from .container import NavigableContainerABC
from .mixins import (
    AddObserverMixin,
    NavigateMixin,
)

logger = logging.getLogger(__name__)


@inject
@dataclass
class BaseModel(
    AddObserverMixin,
):
    """Base class for page view."""

    def __post_init__(self) -> None:
        """Construct the model."""
        self._setup()

    def _setup(self) -> None:
        """Set up the model features."""


@inject
@dataclass
class BaseView(
    NavigableContainerABC[StyleConfig, ThemeConfig],
    ABC,
):
    """Base implementation for page view."""

    _style_config: StyleConfig
    _theme_config: ThemeConfig


@inject
@dataclass
class BaseController(
    ContentABC,
    ABC,
):
    """Abstract base class for controller."""

    def __post_init__(self) -> None:
        """Construct the controller."""
        self._setup()

    def _setup(self) -> None:  # noqa: B027
        """Set up the controller features."""
        pass


@inject
@dataclass
class BasePageController(
    NavigateMixin,
    BaseController,
):
    """Base class for page controller."""

    _view: IView
    _navigator: INavigator

    @override
    def __post_init__(self) -> None:
        """Construct the controller."""
        super().__post_init__()
        self._view.add_observer(self)

    @override
    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._view.content

    def on_open(self, **kwargs: object) -> None:
        """Call methods when page opens."""
        pass
