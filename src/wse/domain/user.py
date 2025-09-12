"""User Use Cases."""

from abc import ABC, abstractmethod

from injector import inject

from wse.data.sources.user import UserObserverABC, UserSource


class UserObserverRegistryUseCaseABC(ABC):
    """ABC for Use Case to register user event notifications."""

    @abstractmethod
    def register_observer(self, observer: UserObserverABC) -> None:
        """Register an observer to receive calculation task updates."""


class UserObserverRegistryUseCase:
    """Use Case to register user event notifications."""

    @inject
    def __init__(self, source: UserSource) -> None:
        """Construct the case."""
        self._source = source

    def register_observer(self, observer: UserObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._source.add_listener(observer)
