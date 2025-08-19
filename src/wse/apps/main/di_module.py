"""Defines Main application module."""

from typing import no_type_check

from injector import Binder, Module

from .http.api_exercises import AssignedExercisesApi
from .http.iapi import IAssignedExercisesApi
from .interfaces import IMainRoutes
from .routes import MainRoutes


class MainRoutesModule(Module):
    """Main application page route module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure binders."""
        binder.bind(IMainRoutes, to=MainRoutes)
        binder.bind(IAssignedExercisesApi, to=AssignedExercisesApi)
