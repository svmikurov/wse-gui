"""Defines base classes of functions features."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import toga

from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.context import HomeContext
from wse.features.shared.button import AppButton
from wse.features.shared.observer import Subject
from wse.features.shared.ui_containers import BaseContent
from wse.interface.ifeatures import IContent, IModel, ISubject, IView


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
    _subject: Subject

    def __init__(self, content_box: BaseContent | None) -> None:
        """Construct the view."""
        self._content = content_box or toga.Box()

        # Listeners
        self._subject = Subject()

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
    def content(self) -> BaseContent:
        """Page content (read-only)."""
        return self._content

    # Notifications
    def _navigate(self, button: toga.Button) -> None:
        self.subject.notify('navigate', navigation_id=button.text)


@dataclass
class BaseController(Subject):
    """Implementation of the base controller."""

    view: IView
    model: IModel | None = None

    def __post_init__(self) -> None:
        """Add sources."""
        self._subject = Subject()
        self.view.subject.add_listener(self)
        if self.model:
            self.model.subject.add_listener(self)

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        return self.view.content

    @property
    def subject(self) -> Subject:
        """Subject of observer pattern (read-only)."""
        return self._subject

    # Notifications
    def navigate(self, navigation_id: NavigationID) -> None:
        """Navigate to page, the button event listener."""
        self._subject.notify('navigate', nav_id=navigation_id)


@dataclass
class BaseContextController(BaseController):
    """Implementation of the base controller of page with model."""

    def _render_context(self) -> None:
        """Render the context to view."""
        self.model.render_context()

    @property
    def content(self) -> IContent:
        """Page content (read-only)."""
        self._render_context()
        return super().content
