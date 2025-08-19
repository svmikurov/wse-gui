"""Defines protocol and ABC for Exercise completion page."""

from abc import ABC, abstractmethod

from typing_extensions import override

from wse.apps.main.http.dto import ExerciseMetaDTO
from wse.features.base import BaseModel, BaseView
from wse.features.base.mvc import BasePageController
from wse.features.interfaces.imvc import IController, IModel, IView


class IExerciseModel(IModel):
    """Protocol for Exercise completion page model interface."""

    def on_open(self, meta: ExerciseMetaDTO) -> None:
        """Call methods when page opens."""


class ExerciseModelABC(BaseModel, IExerciseModel, ABC):
    """Abstract base class for Exercise completion page model."""

    @abstractmethod
    @override
    def on_open(self, meta: ExerciseMetaDTO) -> None:
        """Call methods when page opens."""


class IExerciseView(IView):
    """Protocol for Exercise completion page view interface."""


class ExerciseViewABC(BaseView, IExerciseView, ABC):
    """Abstract base class for Exercise completion page view."""


class IExerciseController(IController):
    """Protocol for Exercise completion page controller."""

    def on_open(self, meta: ExerciseMetaDTO) -> None:
        """Call methods when page opens."""


class ExerciseControllerABC(BasePageController, IExerciseController, ABC):
    """Abstract base class for Exercise completion page controller."""

    # TODO: Fix type ignore via generic typing
    @abstractmethod
    @override
    def on_open(self, meta: ExerciseMetaDTO) -> None:  # type: ignore[override]
        """Call methods when page opens."""
