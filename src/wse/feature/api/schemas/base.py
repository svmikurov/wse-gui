"""Base `pydantic` v1 schema."""

from pydantic import BaseModel
from wse_exercises.base.mixins import ConvertMixin


class BaseSchema(ConvertMixin, BaseModel):
    """Base pydantic model with conversion between dict/json."""
