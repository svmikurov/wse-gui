"""Defines shared features injection container."""

from typing import no_type_check

from injector import Binder, Module

from wse.features.services.exercise import ExerciseService

from .interfaces import IExerciseService


class FeatureServicesModule(Module):
    """Feature services injection container."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure bindings."""
        binder.bind(IExerciseService, to=ExerciseService)
