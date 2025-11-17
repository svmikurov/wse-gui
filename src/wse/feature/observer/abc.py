"""Abstract Base Classes protocols for Observer pattern components."""

from abc import ABC, abstractmethod
from typing import Generic, Literal, override

import toga

from wse.types import AccessorT, NotifyT

from .generic import NotifyGenABC, ObserverManagerGenABC

ChangeNotifyT = Literal['change']


class ObserverManagerABC(ObserverManagerGenABC[object], ABC):
    """ABC for observer adding."""

    @property
    @override
    @abstractmethod
    def observers(self) -> list[object]:
        """Get observers."""

    @abstractmethod
    @override
    def add_observer(self, observer: object) -> None:
        """Add a new observer to this subject."""

    @abstractmethod
    @override
    def remove_observer(self, observer: object) -> None:
        """Remove an observer from this subject."""


class NotifyABC(NotifyGenABC[str], ABC):
    """ABC for observer notification."""

    @abstractmethod
    @override
    def notify(self, notification: str, **kwargs: object) -> None:
        """Notify all observers an event has occurred."""


class SubjectABC(
    ObserverManagerABC,
    NotifyABC,
    ABC,
):
    """ABC for Subject of Observer pattern."""


# Observer via accessor
# ---------------------


class AccessorNotifyGenABC(ABC, Generic[NotifyT, AccessorT]):
    """ABC for observer notification via accessor."""

    @abstractmethod
    def notify(
        self,
        notification: NotifyT,
        accessor: AccessorT,
        **kwargs: object,
    ) -> None:
        """Notify all observers an event has occurred."""


class AccessorABC(ABC):
    """ABC for listener via accessor."""

    @abstractmethod
    def _check_accessors(self) -> None:
        """Check that UI attr name corresponding to accessor."""

    @abstractmethod
    def _get_ui(self, accessor: str) -> toga.Widget:
        """Get UI via accessor."""


# TODO: Add methods: `add`, `insert`, `remove`, `clear`


class UpdateObserverABC(ABC, Generic[AccessorT]):
    """ABC for 'update' observer accessor event."""

    @abstractmethod
    def set_values(self, accessor: AccessorT, value: object) -> None:
        """Update observer accessor."""


class ChangeObserverABC(ABC, Generic[AccessorT]):
    """ABC for 'change' observer accessor event."""

    @abstractmethod
    def change(self, accessor: AccessorT, value: object) -> None:
        """Change observer accessor."""
