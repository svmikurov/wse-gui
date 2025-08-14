"""Defines configuration for Core app API."""

from wse.config.settings import ApiConfig


class ExercisesApiConfig(ApiConfig):
    """Configuration for Exercises API url paths."""

    assigned_exercises: str
