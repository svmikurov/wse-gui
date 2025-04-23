"""Defines protocol interfaces for application components.

This module contains abstract interfaces (protocols) that define
the expected structure and behavior of key application components.
"""

from abc import abstractmethod
from typing import Protocol

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.object_id import ObjectID


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

    def add(self, *children: toga.Widget) -> None:
        """Add a widgets to page content."""

    @property
    def children(self) -> list[toga.Widget]:
        """The children of content node."""


class IContext(Protocol):
    """Protocol defining the interface for page context components."""


class IModel(Protocol):
    """Protocol defining the interface for model components."""

    def render_context(self) -> None:
        """Render the context to view."""

    @property
    def subject(self) -> ISubject:
        """Model subject."""

    @property
    def context(self) -> IContext:
        """View context."""


class IContainer(Protocol):
    """Protocol defining the interface for widget container."""

    @property
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""

    @property
    def content(self) -> IContent:
        """Get the page content."""

    def get_content_widgets(self) -> list[toga.Widget]:
        """Return content widgets."""

    def localize_ui(self) -> None:
        """Update all UI elements with current translations."""


class IView(IContainer, Protocol):
    """Protocol defining the interface for view components."""

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


class IContextController(IController, Protocol):
    """Protocol defining the interface for controller with context."""

    model: IModel

    def request_context(self) -> None:
        """Request context from the model."""
