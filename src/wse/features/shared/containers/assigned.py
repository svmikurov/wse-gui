"""Assigned exercises container."""

from dataclasses import dataclass
from functools import partial

from injector import inject
from toga import Box, Button, Column, Label
from toga.style import Pack
from typing_extensions import override

from wse.apps.main.http.dto import AssignedExercisesDTO
from wse.config.layout import StyleConfig, ThemeConfig
from wse.features.base.mixins import AddObserverMixin, GetContentMixin

from .iabc.iassigned import AssignedContainerABC

# Widgets are created dynamically with a specific ID prefix.
INNER_BOX_PREFIX = '_inner'
LABEL_PREFIX = '_label'
BUTTON_PREFIX = '_button'


@inject
@dataclass
class AssignedContainer(
    GetContentMixin,
    AddObserverMixin,
    AssignedContainerABC,
):
    """Container for Assigned exercises."""

    _style: StyleConfig
    _theme: ThemeConfig

    @override
    def add_exercise(self, exercise: AssignedExercisesDTO) -> None:
        """Add exercise to specific mentor exercises box."""
        inner_box = self._get_or_create_inner_box(exercise)
        button = Button(
            id=self._get_button_id(exercise),
            text=exercise.exercise_name,
            style=Pack(**self._style.button, **self._theme.button),
            on_press=partial(
                self._select, assignation_id=exercise.assignation_id
            ),
        )
        inner_box.add(button)

    def update_exercises(self, exercises: list[AssignedExercisesDTO]) -> None:
        """Update exercises."""
        self.remove_exercises()
        for exercise in exercises:
            self.add_exercise(exercise)

    @override
    def remove_exercises(self) -> None:
        """Remove all exercises."""
        self.content.clear()

    def _get_or_create_inner_box(self, exercise: AssignedExercisesDTO) -> Box:
        """Get existing or create new inner box for mentor exercises.

        :param AssignedExercisesDTO exercise: Assigned exercise DTO
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
                    **self._style.label_title,
                    **self._theme.label_title,
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
        self._notify('exersice_selected', value=assignation_id)

    # Utility methods

    @staticmethod
    def _get_inner_id(exercise: AssignedExercisesDTO) -> str:
        return f'{INNER_BOX_PREFIX}_{exercise.mentorship_id}'

    @staticmethod
    def _get_label_id(exercise: AssignedExercisesDTO) -> str:
        return f'{LABEL_PREFIX}_{exercise.mentorship_id}'

    @staticmethod
    def _get_button_id(exercise: AssignedExercisesDTO) -> str:
        return f'{BUTTON_PREFIX}_{exercise.assignation_id}'
