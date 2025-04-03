"""Defines protocol interfaces for application components.

This module contains abstract interfaces (protocols) that define
the expected structure and behavior of key application components.
"""

# ruff: noqa: D101, D102, D204, E301, E302

from abc import abstractmethod
from typing import Protocol, runtime_checkable


@runtime_checkable
class ISubject:
    """An observable object in the Observer pattern."""

    @abstractmethod
    def add_listener(self, listener: object) -> None:
        """Register an observer to receive notifications."""

    @abstractmethod
    def notify(self, notification: str, **kwargs: object) -> None:
        """Register an observer to receive notifications."""


@runtime_checkable
class IModel(Protocol):
    """Protocol defining the interface for model components."""

    @property
    @abstractmethod
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""


@runtime_checkable
class IView(Protocol):
    """Protocol defining the interface for view components."""

    @property
    @abstractmethod
    def subject(self) -> ISubject:
        """Get the subject for observer pattern notifications."""


@runtime_checkable
class IController(Protocol):
    """Protocol defining the interface for controller components."""
