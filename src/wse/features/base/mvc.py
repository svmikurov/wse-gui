"""Defines base class for MVC model components."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.config.layout import LayoutConfig
from wse.core.interfaces import INavigator

from ..apps.nav_id import NavID
from ..interfaces import IContent, ISubject, IView
from .mixins import CreateNavButtonMixin, SubscribeObserverMixin


@dataclass
class BaseView(
    CreateNavButtonMixin,
    SubscribeObserverMixin,
    ABC,
):
    """Abstract base class for page view."""

    _content: IContent
    _subject: ISubject
    _config: LayoutConfig

    def __post_init__(self) -> None:
        """Construct the view."""
        self._create_ui()
        self.localize_ui()
        self.update_style()
        self._populate_content()

    @abstractmethod
    def _create_ui(self) -> None:
        """Create UI."""

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize the UI text."""

    @abstractmethod
    def update_style(self) -> None:
        """Update widgets style."""

    @abstractmethod
    def _populate_content(self) -> None:
        """Populate view content with UI."""

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._content


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
