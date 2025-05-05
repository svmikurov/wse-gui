"""Defines Practice page controller."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from wse.core.navigation.navigation_id import NavigationID
from wse.interface.ifeatures import IContent
from wse.interface.iobserver import ISubject

if TYPE_CHECKING:
    from wse.features.examples import ExamplesView

logger = logging.getLogger(__name__)


@dataclass
class ExamplesController:
    """Practice page controller."""

    view: ExamplesView
    _subject: ISubject

    def __post_init__(self) -> None:
        """Subscribe to service layer."""
        # Subscribe to view notifications
        self.view.button_handler.subject.add_listener(self)

    def on_open(self) -> None:
        """Call methods on page open event."""
        pass

    # -=== Listening to View notification ===-

    def navigate(self, nav_id: NavigationID) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', nav_id=nav_id)

    # -=== Utility methods ===-

    @property
    def subject(self) -> ISubject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self.view.content
