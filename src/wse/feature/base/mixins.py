"""Defines mixins for features base classes."""

from dataclasses import dataclass
from typing import Generic, TypeVar

from wse.core.navigation.nav_id import NavID

from ..interfaces.icontent import ContentProto
from ..interfaces.imvc import ModelProto
from ..interfaces.iobserver import ObserverProto, SubjectABC
from ..interfaces.types import NotifyT, ObserverT

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

    _subject: SubjectABC

    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""
        self._subject.notify('navigate', nav_id=nav_id)


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

    _subject: SubjectABC

    def add_observer(self, observer: ObserverProto) -> None:
        """Register an observer to receive calculation task updates."""
        self._subject.add_observer(observer)

    def remove_observer(self, observer: ObserverProto) -> None:
        """Remove observer from subject observers."""
        self._subject.remove_observer(observer)

    def _notify(self, notification: str, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)


@dataclass
class AddObserverGen(Generic[NotifyT]):
    """Mixin that enables observer subscription capability.

    **DEPRECATED** Will be removed, use `AddObserverGenT`.
    """

    _subject: SubjectABC

    def add_observer(self, observer: ObserverT) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def remove_observer(self, observer: ObserverT) -> None:
        """Remove observer."""
        self._subject.remove_observer(observer)

    def _notify(self, notification: NotifyT, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)

    @property
    def observers(self) -> list[ObserverT]:
        """Get observers."""
        return self._subject.observers  # type: ignore[return-value]


@dataclass
class AddObserverGenT(Generic[ObserverT, NotifyT]):
    """Mixin that enables observer subscription capability."""

    _subject: SubjectABC

    def add_observer(self, observer: ObserverT) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def remove_observer(self, observer: ObserverT) -> None:
        """Remove observer from subject observers."""
        self._subject.remove_observer(observer)

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
