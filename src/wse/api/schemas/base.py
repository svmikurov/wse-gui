"""Base `pydantic` v1 schema."""

from typing import Any

from pydantic import BaseModel
from wse_exercises.base.mixins import ConvertMixin


class BaseSchema(ConvertMixin, BaseModel):
    """Base pydantic model with conversion between dict/json."""


class IdNameSchema(BaseSchema):
    """Schema representing an entity with an identifier and a name."""

    id: int
    name: str


class CodeNameSchema(BaseSchema):
    """Schema representing an entity with a code and a name."""

    code: str
    name: str


class ItemsData(BaseSchema):
    """Response items data."""

    count: int
    next: str | None
    previous: str | None
    results: list[Any]
