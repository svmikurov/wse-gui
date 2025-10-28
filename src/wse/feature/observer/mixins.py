"""Defines mixins for features base classes."""

from dataclasses import dataclass
from typing import Generic

from wse.core.navigation.nav_id import NavID
from wse.types import NotifyT, ObserverT

from .abc import SubjectABC
from .generic import NotifyGenABC, ObserverManagerGenABC


@dataclass
class ObserverManagerGen(ObserverManagerGenABC[ObserverT]):
    """Mixin that enables observer subscription capability."""

    _subject: SubjectABC

    def add_observer(self, observer: ObserverT) -> None:
        """Subscribe observer an event has occurred."""
        self._subject.add_observer(observer)

    def remove_observer(self, observer: ObserverT) -> None:
        """Remove observer from subject observers."""
        self._subject.remove_observer(observer)

    @property
    def observers(self) -> list[ObserverT]:
        """Get observers."""
        return self._subject.observers  # type: ignore[return-value]


class NotifyGen(NotifyGenABC[NotifyT]):
    """Notify observer about event."""

    _subject: SubjectABC

    def notify(self, notification: NotifyT, **kwargs: object) -> None:
        """Notify observer about event."""
        self._subject.notify(notification, **kwargs)


@dataclass
class SubjectGen(
    ObserverManagerGen[ObserverT],
    NotifyGen[NotifyT],
    Generic[ObserverT, NotifyT],
):
    """Mixin that enables observer subscription capability."""


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
class ObserverManager(ObserverManagerGen[object]):
    """Mixin that enables observer subscription capability."""

    _subject: SubjectABC

    def add_observer(self, observer: object) -> None:
        """Register an observer to receive calculation task updates."""
        self._subject.add_observer(observer)

    def remove_observer(self, observer: object) -> None:
        """Remove observer from subject observers."""
        self._subject.remove_observer(observer)

    @property
    def observers(self) -> list[object]:
        """Get observers."""
        return self._subject.observers


class AddNotifyMixin:
    """Mixin providing observe notification."""

    _subject: SubjectABC

    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify observers."""
        self._subject.notify(notification, **kwargs)
