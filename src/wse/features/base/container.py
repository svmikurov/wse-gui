"""Defines base widget container."""

from abc import ABC, abstractmethod

import toga

from wse.features.shared.observer import Subject
from wse.features.shared.ui_containers import BaseContent
from wse.interface.ifeatures import IContent, ISubject
from wse.pages.widgets import AppButton


class BaseContainer(ABC):
    """Widget base container."""

    def __init__(
        self,
        content_box: IContent | None = None,
        subject: ISubject | None = None,
    ) -> None:
        """Construct the view."""
        self._content = (
            content_box if content_box is not None else BaseContent()
        )
        self._subject = subject if subject is not None else Subject()

        # Add UI
        self._create_ui()
        self._assign_ui_text()

    # UI create methods
    @abstractmethod
    def _create_ui(self) -> None:
        """Create a user interface."""

    @abstractmethod
    def _assign_ui_text(self) -> None:
        """Assign a text for user interface widgets."""

    # Utility methods
    def _create_nav_btn(self) -> toga.Button:
        return AppButton(on_press=self._navigate)

    @property
    def subject(self) -> Subject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content

    # Notifications
    def _navigate(self, button: toga.Button) -> None:
        self.subject.notify('navigate', nav_id=button.text)
