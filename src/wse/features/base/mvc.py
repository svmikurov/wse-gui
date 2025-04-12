"""Defines base classes of functions features."""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import toga
from typing_extensions import override

from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.context import HomeContext
from wse.features.shared.button import AppButton
from wse.features.shared.observer import Subject
from wse.interface.ifeatures import IContent, IModel, ISubject, IView

logger = logging.getLogger(__name__)


class BaseModel(ABC):
    """Base page model."""

    def __init__(self, subject: ISubject) -> None:
        """Construct the model."""
        super().__init__()
        self._subject = subject
        self._context = HomeContext()

    def render_context(self) -> None:
        """Render the context to view."""
        self._set_context()
        self._notify_render_context()

    @abstractmethod
    def _set_context(self) -> None:
        """Set view context for render into view."""

    @abstractmethod
    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject

    @property
    def context(self) -> HomeContext:
        """View context."""
        return self._context


class BaseView:
    """Implementation of the base view."""

    _label_title: toga.Label

    def __init__(
        self,
        content_box: IContent | None = None,
        subject: ISubject | None = None,
    ) -> None:
        """Construct the view."""
        self._content = content_box if content_box is not None else toga.Box()
        self._subject = subject if subject is not None else Subject()

    # Utility methods
    def _create_nav_btn(self) -> toga.Button:
        return AppButton(on_press=self._navigate)

    @property
    def subject(self) -> Subject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    @property
    def title(self) -> str:
        """Page title (read-only)."""
        return self._label_title.text

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self._content

    # Notifications
    def _navigate(self, button: toga.Button) -> None:
        self.subject.notify('navigate', nav_id=button.text)


@dataclass(kw_only=True)
class BaseController(Subject):
    """Implementation of the base controller."""

    view: IView
    _subject: Subject = field(default_factory=Subject)

    def __post_init__(self) -> None:
        """Add sources."""
        self.view.subject.add_listener(self)

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self.view.content

    @property
    def subject(self) -> Subject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    # Notifications
    def navigate(self, nav_id: NavigationID) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', nav_id=nav_id)


@dataclass(kw_only=True)
class BaseContextController(BaseController):
    """Implementation of the base controller of page with model."""

    model: IModel

    @override
    def __post_init__(self) -> None:
        """Subscribe the controller to listen to the model."""
        super().__post_init__()
        self.model.subject.add_listener(self)

    @property
    @override
    def content(self) -> IContent:
        """Page content (read-only)."""
        self._render_context()
        return super().content

    def _render_context(self) -> None:
        """Render the context to view."""
        self.model.render_context()
