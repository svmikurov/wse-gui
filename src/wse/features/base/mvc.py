"""Defines base class for MVC model components."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.interfaces import INavigator

from ..interfaces import IContent, ISubject, IView
from ..subapps.nav_id import NavID
from .container import BaseContainer
from .mixins import AddObserverMixin, CreateNavButtonMixin


@dataclass
class BaseModel(
    AddObserverMixin,
):
    """Base class for page view."""

    _subject: ISubject

    def __post_init__(self) -> None:
        """Construct the model."""
        self._setup()

    def _setup(self) -> None:
        """Set up the model features."""


@dataclass
class BaseView(
    BaseContainer,
    CreateNavButtonMixin,
    ABC,
):
    """Abstract base class for page view."""

    _style_config: StyleConfig
    _theme_config: ThemeConfig

    def __post_init__(self) -> None:
        """Construct the view."""
        super().__post_init__()
        self.update_style(self._style_config)
        self.update_style(self._theme_config)

    @abstractmethod
    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style.

        For example:
            def update_style(
                self, config: StyleConfig | ThemeConfig
            ) -> None:
                self._label_title.style.update(**config.title)
                ...
        """


# TODO: Refactor base controller without navigate feature
#  to avoid SOLID error,
#  this base class contains navigation and adds observer for view.
@dataclass
class BaseController:
    """Base class for page controller."""

    _view: IView
    _navigator: INavigator

    def __post_init__(self) -> None:
        """Construct the controller."""
        self._view.add_observer(self)
        self._setup()

    def _setup(self) -> None:
        """Set up the controller features."""
        pass

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
        self._navigator.navigate(nav_id)

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._view.content
