"""Abstract Base Classes for User domain logic Use Cases."""

from abc import ABC, abstractmethod

from typing_extensions import override

from wse.data.sources.user import UserObserverABC
from wse.domain.abc import SubscribeUseCaseABC


class UserObserverRegistryUseCaseABC(
    SubscribeUseCaseABC[UserObserverABC],
    ABC,
):
    """ABC for Use Case to register user event notifications."""

    @abstractmethod
    @override
    def add_listener(self, observer: UserObserverABC) -> None:
        """Register an observer on User event notifications."""

    @abstractmethod
    @override
    def remove_listener(self, observer: UserObserverABC) -> None:
        """Delete an observer from User event notifications."""
