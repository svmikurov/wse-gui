"""Defines protocol interfaces for application components.

This module contains abstract interfaces (protocols) that define
the expected structure and behavior of key application components.
"""

from typing import Protocol

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.object_id import ObjectID
from wse.interface.iobserver import ISubject


class IContent(Protocol):
    """Protocol defining the interface for page content components."""

    @property
    def id(self) -> ObjectID | str:
        """Get the object test ID."""

    @id.setter
    def id(self, value: ObjectID) -> None:
        """Get the object test ID."""

    def add(self, *children: toga.Widget) -> None:
        """Add a widgets to page content."""

    @property
    def children(self) -> list[toga.Widget]:
        """The children of content node."""


class IContext(Protocol):
    """Protocol defining the interface for page context components."""


# Model


class IModel(Protocol):
    """Protocol defining the interface for model components."""

    def render_context(self) -> None:
        """Render the context to view."""

    @property
    def subject(self) -> ISubject:
        """Model subject."""

    # TODO: remove from interface?
    @property
    def context(self) -> IContext:
        """View context."""


# Controller


class IEventRunner(Protocol):
    """Protocol defining the interface for start event on page open."""

    def on_open(self, *args: object, **kwargs: object) -> None:
        """Perform events on page open."""


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


class IContextController(IController, IEventRunner, Protocol):
    """Protocol defining the interface for controller with context."""

    model: IModel

    def request_context(self) -> None:
        """Request context from the model."""


# View


class IContainer(Protocol):
    """Protocol defining the interface for widget container."""

    @property
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""

    @property
    def content(self) -> IContent:
        """Get the page content."""

    def localize_ui(self) -> None:
        """Update all UI elements with current translations."""


class IView(IContainer, Protocol):
    """Protocol defining the interface for view components."""

    @property
    def title(self) -> str:
        """Get the page title."""
