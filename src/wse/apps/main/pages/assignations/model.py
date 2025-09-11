"""Defines Assigned exercises page model."""

from dataclasses import dataclass
from typing import Literal

from injector import inject
from typing_extensions import override

from wse.apps.main.api import AssignationsApiProto
from wse.feature.base.mixins import AddObserverGen
from wse.feature.shared.schemas.exercise import ExerciseMeta

from .abc import AssignationsModelABC, AssignationsModelFeature

_NotifyType = Literal['exercises_updated']


class _Feature(
    AssignationsModelFeature,
    AddObserverGen[_NotifyType],
):
    """Assigned page model feature."""

    _api_service: AssignationsApiProto

    @override
    def fetch_exercises(self) -> None:
        """Fetch assigned exercises."""
        exercises = self._api_service.request_all_exercises()
        if exercises is not None:
            self._notify('exercises_updated', exercises=exercises)

    @override
    def fetch_exercise(
        self,
        assignation_id: str,
    ) -> ExerciseMeta | None:
        """Fetch assigned exercise meta data."""
        return self._api_service.request_selected(assignation_id)


@inject
@dataclass
class AssignationsModel(
    _Feature,
    AssignationsModelABC,
):
    """Assigned exercises page model."""

    _api_service: AssignationsApiProto
