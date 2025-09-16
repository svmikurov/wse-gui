"""User Use Cases."""

from injector import inject
from typing_extensions import override

from wse.data.sources.user import UserObserverABC, UserSource

from .abc import (
    UserObserverRegistryUseCaseABC,
)


class UserObserverRegistryUseCase(UserObserverRegistryUseCaseABC):
    """Use Case to register user event notifications."""

    @inject
    def __init__(self, source: UserSource) -> None:
        """Construct the case."""
        self._source = source

    @override
    def add_observer(self, observer: UserObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._source.add_listener(observer)

    @override
    def remove_observer(self, observer: UserObserverABC) -> None:
        """Delete an observer from User event notifications."""
        self._source.remove_listener(observer)
