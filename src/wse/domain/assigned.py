"""Assigned exercise Use Cases."""
from injector import inject

from ..data.sources.assigned import (
    AssignedSource,
    AssignedSourceObserverABC,
)
from .abc import AssignedObserverRegistryUseCaseABC


class AssignedObserverRegistryUseCase(AssignedObserverRegistryUseCaseABC):
    """Assigned exercise source observer registry the Use Case."""

    @inject
    def __init__(self, source: AssignedSource) -> None:
        """Construct the registry."""
        self._source = source

    def register_observer(self, observer: AssignedSourceObserverABC) -> None:
        """Register an observer to receive calculation task updates."""
        self._source.add_listener(observer)


class AssignedLogicUseCase:
    """Assigned exercise logic Use Case."""

    @inject
    def __init__(
        self,
        repository: ...,
    ) -> None:
        """Construct the case."""
        self._repository = repository
        self._repository.add_observer(self)

    def result_updated(self, is_correct: bool) -> None:
        """Handle the answer check result."""
        if is_correct:
            self._repository.fetch_task()
        else:
            self._repository.update_solution()
