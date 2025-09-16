"""Assigned exercises container."""

import logging
from dataclasses import dataclass
from functools import partial

from injector import inject
from toga import Box, Button, Column, Label
from toga.style import Pack
from typing_extensions import override

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base.mixins import AddObserverMixin, GetContentMixin
from wse.feature.shared.containers.assigned.abc import (
    AssignationsContainerABC,
)
from wse.feature.shared.schemas.exercise import ExerciseInfo

audit = logging.getLogger(__name__)

# Widgets are created dynamically with a specific ID prefix.
INNER_BOX_PREFIX = '_inner'
LABEL_PREFIX = '_label'
BUTTON_PREFIX = '_button'


@inject
@dataclass
class AssignationsContainer(
    GetContentMixin,
    AddObserverMixin,
    AssignationsContainerABC,
):
    """Container for Assigned exercises."""

    _style: StyleConfig
    _theme: ThemeConfig

    @override
    def add_exercise(self, exercise: ExerciseInfo) -> None:
        """Add exercise to specific mentor exercise enumeration box."""
        inner_box = self._get_or_create_inner_box(exercise)
        button = Button(
            id=self._get_button_id(exercise),
            text=exercise.exercise_name,
            style=Pack(
                **self._style.assigned.button,  # type: ignore[arg-type]
                **self._theme.assigned.button,  # type: ignore[arg-type]
            ),
            on_press=partial(
                self._select, assignation_id=exercise.assignation_id
            ),
        )
        inner_box.add(button)

    @override
    def update_exercises(self, exercises: list[ExerciseInfo]) -> None:
        """Update exercise enumeration."""
        self.remove_exercises()
        for exercise in exercises:
            self.add_exercise(exercise)

    @override
    def remove_exercises(self) -> None:
        """Remove all exercises."""
        self.content.clear()

    def _get_or_create_inner_box(self, exercise: ExerciseInfo) -> Box:
        """Get existing or create new inner box for mentor exercises.

        :param ExerciseInfo exercise: Assigned exercise
        :return: Existing or newly created exercises container
        :rtype: toga.Box
        """
        inner_box_id = self._get_inner_id(exercise)
        inner_box = self.content.get_by_id(inner_box_id)

        if inner_box is None:
            label = Label(
                id=self._get_label_id(exercise),
                text=exercise.mentor_username,
                style=Pack(
                    **self._style.assigned.label,  # type: ignore[arg-type]
                    **self._theme.assigned.label,  # type: ignore[arg-type]
                ),
            )
            inner_box = Column(
                id=inner_box_id,
                children=[label],
            )
            self.content.add(inner_box)

        return inner_box

    # Callback function

    def _select(self, _: Button, assignation_id: str) -> None:
        """Notify observer that exercise selected."""
        self._notify('exercise_selected', assignation_id=assignation_id)

    # Utility methods

    @staticmethod
    def _get_inner_id(exercise: ExerciseInfo) -> str:
        return f'{INNER_BOX_PREFIX}_{exercise.mentorship_id}'

    @staticmethod
    def _get_label_id(exercise: ExerciseInfo) -> str:
        return f'{LABEL_PREFIX}_{exercise.mentorship_id}'

    @staticmethod
    def _get_button_id(exercise: ExerciseInfo) -> str:
        return f'{BUTTON_PREFIX}_{exercise.assignation_id}'

    def on_close(self) -> None:
        """Call methods before close the screen."""
        audit.debug(
            f'Not implemented `on_close()` for {self.__class__.__name__}'
        )
