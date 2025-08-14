"""Defines Main application module."""

from typing import no_type_check

from injector import Binder, Module, provider, singleton

from wse.config.settings import CONFIGS_PATH
from wse.utils.loader import ApiConfigLoader

from .http.api_exercises import AssignedExercisesApi
from .http.config import ExercisesApiConfig
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

    @singleton
    @provider
    def provide_assigned_api_config(self) -> ExercisesApiConfig:
        """Provide the assigned exercises API config."""
        loader = ApiConfigLoader(
            ExercisesApiConfig,
            CONFIGS_PATH / 'api_exercises.json',
        )
        return loader.load_api_config()
