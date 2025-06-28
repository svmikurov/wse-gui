"""Defines Feature features injection module."""

from typing import no_type_check

from injector import Binder, Module

from ..services.exercise import ExerciseService
from .interfaces import IExerciseService


class FeatureServicesModule(Module):
    """Feature services injection module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(IExerciseService, to=ExerciseService)
