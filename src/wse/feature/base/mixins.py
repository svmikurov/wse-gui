"""Defines mixins for features base classes."""

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable

from ..interfaces.icontent import ContentProto
from ..interfaces.imvc import ModelProto
from ..interfaces.iobserver import Observable, ObserverProto
from ..interfaces.iwidgets import NavigableButton
from ..interfaces.types import NotifyT, ObserverT
from ..shared.widgets.buttons import NavButton

ModelT = TypeVar('ModelT', bound=ModelProto)
OpenT = TypeVar('OpenT')


@dataclass
class SetupMixin:
    """Mixin provides the setup method."""

    def __post_init__(self) -> None:
        """Construct the mixin."""
        self._setup()

    def _setup(self) -> None:
        """Set up a features.

        Override to set up a features on initialize.
        """


@dataclass
class NavigateMixin:
    """Mixin to provide navigation functionality."""

    _navigator: Navigable

    def navigate(self, nav_id: NavID, **kwargs: dict[str, Any]) -> None:
        """Navigate to page."""
        self._navigator.navigate(nav_id, **kwargs)


@dataclass
class NotifyNavigateMixin:
    """Mixin to provide navigation notification.

    Use to pass navigation event notification from view component to
    controller.
    To do this, add a mixin in the view component controller and the
    view controller.

    For example:

        class TopBarController(NotifyNavigateMixin, ...): ...

        class SomePageController((NotifyNavigateMixin, ...):

            _container: ITopBarController

    """

    _subject: Observable

    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""
        self._subject.notify('navigate', nav_id=nav_id)


@dataclass
class CreateNavButtonMixin:
    """Mixin that provides navigation button creation functionality."""

    _subject: Observable

    def _create_nav_btn(self, nav_id: NavID) -> NavigableButton:
        """Create navigation button."""
        return NavButton(nav_id=nav_id, on_press=self._handle_navigate)

    def _handle_navigate(self, button: NavigableButton) -> None:
        """Handle navigation button press."""
        self._subject.notify('navigate', nav_id=button.nav_id)


@dataclass
class GetContentMixin:
    """Mixin to provide content."""

    _content: ContentProto

    @property
    def content(self) -> ContentProto:
        """Get page content."""
        return self._content


@dataclass
class AddObserverMixin:
    """Mixin that enables observer subscription capability."""

    _subject: Observable

    def add_observer(self, observer: ObserverProto) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def _notify(self, notification: str, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)


@dataclass
class AddObserverGen(Generic[NotifyT]):
    """Mixin that enables observer subscription capability.

    **DEPRECATED** Will be removed, use `AddObserverGenT`.
    """

    _subject: Observable

    def add_observer(self, observer: ObserverProto) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def _notify(self, notification: NotifyT, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)

    @property
    def observers(self) -> list[ObserverProto]:
        """Get observers."""
        return self._subject.observers


@dataclass
class AddObserverGenT(Generic[ObserverT, NotifyT]):
    """Mixin that enables observer subscription capability."""

    _subject: Observable

    def add_observer(self, observer: ObserverT) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def _notify(self, notification: NotifyT, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)

    # TODO: Fix type ignore.
    #       Update `Observable` type with `list[ObserverT]` return type.
    @property
    def observers(self) -> list[ObserverT]:
        """Get observers."""
        return self._subject.observers  # type: ignore[return-value]


class ModelObserverMixin(Generic[ModelT]):
    """Mixing providing subscribe to model notification."""

    _model: ModelT

    def _setup(self) -> None:
        """Set up the controller features."""
        self._model.add_observer(self)
