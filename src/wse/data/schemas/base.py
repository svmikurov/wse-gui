"""Base pydantic v1 schema."""

from typing import Any, TypeAlias, Union

from pydantic import BaseModel
from wse_exercises.base.mixins import ConvertMixin

Options: TypeAlias = list['IdName'] | list['CodeName']
Selected: TypeAlias = Union['IdName', 'CodeName']
WordOptions: TypeAlias = Options | Selected


class BaseSchema(ConvertMixin, BaseModel):
    """Base pydantic model with conversion between dict/json."""


class IdName(BaseSchema):
    """Schema representing an entity with an identifier and a name."""

    id: str
    name: str


class CodeName(BaseSchema):
    """Schema representing an entity with a code and a name."""

    code: str
    name: str


class ItemsData(BaseSchema):
    """Response items data."""

    count: int
    next: str | None
    previous: str | None
    results: list[Any]
