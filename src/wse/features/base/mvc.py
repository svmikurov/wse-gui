"""Defines base classes of functions features."""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import toga
from typing_extensions import override

from wse.core.api.client import ApiClient
from wse.core.navigation.navigation_id import NavigationID
from wse.features.base.container import NavigableContainer
from wse.features.base.context import Context
from wse.features.shared.observer import Subject
from wse.interface.ifeatures import IContent, IContext, IModel, ISubject, IView

logger = logging.getLogger(__name__)


class BaseModel(ABC):
    """Base page model."""

    def __init__(
        self,
        api_client: ApiClient | None = None,
        subject: ISubject | None = None,
        context: IContext | None = None,
    ) -> None:
        """Construct the model."""
        self._api_client = api_client
        self._subject = subject if subject is not None else Subject()
        self._context = context if context is not None else Context()

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
    def context(self) -> IContext:
        """View context."""
        return self._context


class BaseView(NavigableContainer, ABC):
    """Implementation of the base view."""

    _label_title: toga.Label

    @property
    def title(self) -> str:
        """Page title (read-only)."""
        return self._label_title.text


########################################################################
# Controllers


@dataclass(kw_only=True)
class BaseController:
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
class ContextController(BaseController):
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
        self.request_context()
        return super().content

    def request_context(self) -> None:
        """Render the context to view."""
        self.model.render_context()
