"""Defines base class for MVC model components."""

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig

from ..interfaces.icontent import ContentProto
from ..interfaces.imvc import ModelProto, ViewProto
from .abstract.mvc import BaseContent
from .container import NavigableContainer
from .mixins import (
    AddObserverMixin,
    NavigateMixin,
    SetupMixin,
)

ModelT = TypeVar('ModelT', bound=ModelProto)
ViewT = TypeVar('ViewT', bound=ViewProto)
DataT = TypeVar('DataT')


# Model


@dataclass
class Model(
    SetupMixin,
    AddObserverMixin,
):
    """Base class for page view."""


# View


@dataclass
class View(
    NavigableContainer[StyleConfig, ThemeConfig],
    ABC,
):
    """Base implementation for page view."""

    _style: StyleConfig
    _theme: ThemeConfig


# Controller


@dataclass
class Controller(
    SetupMixin,
    BaseContent,
    ABC,
):
    """Abstract base class for controller."""


@dataclass
class BasePageController(
    NavigateMixin,
    Controller,
    Generic[ViewT],
):
    """Base class for page controller."""

    _view: ViewT

    @override
    def __post_init__(self) -> None:
        """Construct the controller."""
        super().__post_init__()
        self._view.add_observer(self)

    @override
    @property
    def content(self) -> ContentProto:
        """Get page content."""
        return self._view.content


@dataclass
class PageController(
    NavigateMixin,
    Generic[ModelT, ViewT, DataT],
):
    """Base page controller.."""

    _model: ModelT
    _view: ViewT

    def __post_init__(self) -> None:
        """Construct the controller."""
        self._model.add_observer(self._view)
        self._model.add_observer(self)
        self._view.add_observer(self)

    def on_open(self, value: DataT | None = None) -> None:
        """Call methods when page opens.

        Override to add methods.
        """

    @property
    def content(self) -> ContentProto:
        """Get page content."""
        return self._view.content
