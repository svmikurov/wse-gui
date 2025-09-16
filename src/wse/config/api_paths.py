"""Defines API paths configuration."""

from pydantic import BaseModel


class ApiConfig(BaseModel):
    """Base api configuration."""

    base_url: str
    jwt: dict[str, str]
    assigned_exercises: str
    selected_exercise: str
    initial_data_path: str
    terms: str


class APIConfigV1(ApiConfig):
    """API configuration for v1 version."""


class TaskAPIConfigV1(BaseModel):
    """Task API configuration."""

    get_task: str
    validate_answer: str


class MathAPIConfigV1(BaseModel):
    """Math api configuration."""

    base_url: str
    index: str
    calculation: TaskAPIConfigV1
