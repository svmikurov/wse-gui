"""Defines protocol interfaces for application components.

This module contains abstract interfaces (protocols) that define
the expected structure and behavior of key application components.
"""

# ruff: noqa: D101, D102, D204, E301, E302

from abc import abstractmethod
from typing import Protocol

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.features.object_id import ObjectID


class ISubject:
    """An observable object in the Observer pattern."""

    @abstractmethod
    def add_listener(self, listener: object) -> None:
        """Register an observer to receive notifications."""

    @abstractmethod
    def notify(self, notification: str, **kwargs: object) -> None:
        """Register an observer to receive notifications."""


class IContent(Protocol):
    """Protocol defining the interface for page content components."""

    @property
    def id(self) -> ObjectID | str:
        """Get the object test ID."""


class IContext(Protocol):
    """Protocol defining the interface for page context components."""


class IModel(Protocol):
    """Protocol defining the interface for model components."""

    def render_context(self) -> None:
        """Render the context to view."""

    def _set_context(self) -> None:
        """Set view context for render into view."""

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""

    @property
    def subject(self) -> ISubject:
        """Model subject."""

    @property
    def context(self) -> IContext:
        """View context."""


class IView(Protocol):
    """Protocol defining the interface for view components."""

    def _create_nav_btn(self) -> toga.Button: ...

    def _navigate(self, button: toga.Button) -> None: ...

    @property
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""

    @property
    def content(self) -> IContent:
        """Get the page content."""

    @property
    def title(self) -> str:
        """Get the page title."""


class IController(Protocol):
    """Protocol defining the interface for controller components."""

    @property
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""

    @property
    def content(self) -> IContent:
        """Get the page content."""

    def navigate(self, navigation_id: NavigationID) -> None:
        """Navigate to page, the button event listener."""


class IContextController(IController):
    def _render_context(self) -> None:
        """Render the context to view."""
