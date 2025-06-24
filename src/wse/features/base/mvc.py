"""Defines base class for MVC model components."""

from abc import ABC
from dataclasses import dataclass

from wse.core.interfaces import INavigator

from ..interfaces import IContent, IView
from ..subapps.nav_id import NavID
from .containers import BaseContainer
from .mixins import (
    CreateNavButtonMixin,
)


@dataclass
class BaseView(
    BaseContainer,
    CreateNavButtonMixin,
    ABC,
):
    """Abstract base class for page view."""


@dataclass
class BaseController:
    """Base class for page controller."""

    _view: IView
    _navigator: INavigator

    def __post_init__(self) -> None:
        """Construct the controller."""
        self._view.add_observer(self)

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
        self._navigator.navigate(nav_id)

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._view.content
