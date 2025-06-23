"""Defines base class for MVC model components."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from wse.config.layout import StyleConfig, ThemeConfig
from wse.core.interfaces import INavigator

from ..interfaces import IContent, ISubject, IView
from ..subapps.nav_id import NavID
from .mixins import (
    AddObserverMixin,
    CreateNavButtonMixin,
    GetContentMixin,
)


@dataclass
class BaseView(
    GetContentMixin,
    AddObserverMixin,
    CreateNavButtonMixin,
    ABC,
):
    """Abstract base class for page view."""

    _content: IContent
    _subject: ISubject
    _style_config: StyleConfig
    _theme_config: ThemeConfig

    def __post_init__(self) -> None:
        """Construct the view."""
        self._create_ui()
        self.localize_ui()
        self.update_style(self._style_config)
        self.update_style(self._theme_config)
        self._populate_content()

    @abstractmethod
    def _create_ui(self) -> None:
        """Create UI.

        For example:
            def _create_ui(self) -> None:
                self._label_title = toga.Label('')
                ...
        """

    @abstractmethod
    def localize_ui(self) -> None:
        """Localize the UI text.

        For example:
            def localize_ui(self) -> None:
                self._label_title.text = label_('Home page title')
                ...
        """

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

    @abstractmethod
    def _populate_content(self) -> None:
        """Populate view content with UI.

        For example:
            def _populate_content(self) -> None:
                self._content.add(
                    self._label_title,
                    ...
                )
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
