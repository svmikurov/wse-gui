"""Defines interface for MVC model controller."""

from typing import Protocol

from wse.core.navigation.navigation_id import NavID
from wse.interface.ifeatures.icontent import IContent
from wse.interface.ifeatures.imvc import IView
from wse.interface.iobserver import ISubject


class IController(Protocol):
    """Practice page controller."""

    view: IView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Subscribe to service layer."""

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page, the button event listener."""

    @property
    def subject(self) -> ISubject:
        """Subject of observer pattern (read-only)."""

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
