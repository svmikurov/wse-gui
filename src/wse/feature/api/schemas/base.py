"""Base `pydantic` v1 schema."""

from typing import Any

from pydantic import BaseModel
from wse_exercises.base.mixins import ConvertMixin


class BaseSchema(ConvertMixin, BaseModel):
    """Base pydantic model with conversion between dict/json."""


class ItemsData(BaseSchema):
    """Response items data."""

    count: int
    next: str | None
    previous: str | None
    results: list[Any]
