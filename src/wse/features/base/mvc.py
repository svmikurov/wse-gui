"""Defines base class for MVC model components."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.interfaces import INavigator

from ..interfaces import IContent, IView
from ..subapps.nav_id import NavID
from .containers import BaseContainer
from .mixins import CreateNavButtonMixin


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
