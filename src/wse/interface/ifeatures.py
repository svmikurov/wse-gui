"""Defines protocol interfaces for application components.

This module contains abstract interfaces (protocols) that define
the expected structure and behavior of key application components.
"""

from typing import Protocol

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.features.shared.enums.object_id import ObjectID
from wse.interface.iexercise import IAnswer
from wse.interface.iobserver import ISubject

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off


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
    def __getitem__(self, item: str) -> str:
        """Get item."""
    def __setitem__(self, key: str, value: str) -> None:
        """Set item."""

# Model


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

# Controller

class IOnPageOpen(Protocol):
    """Protocol defining the interface for start event on page open."""
    def on_open(self, *args: object, **kwargs: object) -> None:
        """Perform events on page open."""


class IController(IOnPageOpen, Protocol):
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


# Specific components


class IExerciseModel(Protocol):
    def on_open(self) -> None:
        """Call methods on page open event."""
    def start_exercise(self) -> None:
        """Start exercise."""
    def get_user_answer(self) -> IAnswer:
        """Get user answer."""
    def handel_answer(self) -> None:
        """Handel user answer."""
    @property
    def subject(self) -> ISubject:
        """Model subject."""
