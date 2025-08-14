"""Defines protocols and ABC for Assigned exercises page."""

from abc import ABC, abstractmethod
from typing import Protocol

from typing_extensions import override

from wse.apps.main.http.dto import AssignedExercisesDTO
from wse.features.interfaces.imvc import IModel, IPageController, IView
from wse.features.interfaces.iobserver import IObserver


class IAssignedModel(IModel, Protocol):
    """Protocol for Assigned exercises page model interface."""

    def on_open(self) -> None:
        """Call methods when page opens."""


class AssignedModelABC(IAssignedModel, ABC):
    """Abstract base class for Assigned exercises model."""

    @abstractmethod
    @override
    def on_open(self) -> None:
        """Call methods when page opens."""

    @abstractmethod
    @override
    def add_observer(self, observer: IObserver) -> None:
        """Add a new observer to this subject."""


class IAssignedView(IView, Protocol):
    """Protocol for Assigned exercise page view interface."""

    def update_exercises(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update exercises to display."""


class AssignedViewABC(IAssignedView, Protocol):
    """Absract base class for Assigned exercise page."""

    @abstractmethod
    @override
    def update_exercises(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update exercises to display."""


class IAssignedController(IPageController, Protocol):
    """Protocol for Assigned exercises page controller interface."""

    # Notifications from model

    def exercises_updated(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update view on update exercises event."""


class AssignedControllerABC(IAssignedController, ABC):
    """Abstract base class for Assigned exercises page."""

    # Notifications from model

    @abstractmethod
    @override
    def exercises_updated(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update view on update exercises event."""
