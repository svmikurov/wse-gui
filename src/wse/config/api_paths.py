"""Defines API paths configuration."""

from pydantic import BaseModel


class ApiConfig(BaseModel):
    """Base api configuration."""

    base_url: str
    jwt: dict[str, str]
    assigned_exercises: str
    selected_exercise: str


class APIConfigV1(ApiConfig):
    """API configuration for v1 version."""
