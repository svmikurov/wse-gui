"""Defines Main Math page controller."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override
from wse_exercises.core.mathem.enums import Exercises

from wse.features.base.mvc import BasePageController
from wse.features.subapps.nav_id import NavID

from .interfaces import (
    IIndexMathController,
    IIndexMathModel,
    IIndexMathView,
)


@inject
@dataclass
class IndexMathController(
    BasePageController,
    IIndexMathController,
):
    """Main Math page controller."""

    _model: IIndexMathModel
    _view: IIndexMathView

    @override
    def _setup(self) -> None:
        self._model.add_observer(self)

    @override
    def on_open(self, **kwargs: object) -> None:
        """Call methods when page opens."""
        self._model.on_open()

    # Notifications from Model

    @override
    def exercises_updated(self, values: list[Exercises]) -> None:
        """Update exercises selection data source."""
        self._view.update_exercise_selection(values)

    @override
    def exercise_started(self, value: Exercises) -> None:
        """Navigate to exercise page."""
        self._navigator.navigate(NavID.SIMPLE_CALC, exercise=value)

    # Notifications from view

    @override
    def exercise_changed(self, value: Exercises) -> None:
        """Handle the change of exercise type."""
        self._model.change_exersice(value)

    @override
    def start_button_pressed(self) -> None:
        """Handle the start exercise button pressed."""
        self._model.start_exercise()
