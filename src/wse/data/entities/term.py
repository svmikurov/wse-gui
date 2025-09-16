"""Defines Term entity."""

from datetime import datetime

from wse.feature.base import BaseSchema


class Term(BaseSchema):
    """Term entity."""

    id: str
    name: str
    definition: str
    created_at: datetime
