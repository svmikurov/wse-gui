"""Glossary HTTP response schemas."""

from datetime import datetime

from ..schemas.base import BaseSchema, ItemsData


class TermSchema(BaseSchema):
    """Term entity."""

    id: str
    name: str
    definition: str
    created_at: datetime


class TermsData(ItemsData):
    """Terms data schema."""

    results: list[TermSchema]


class TermPresentationParamsSchema(BaseSchema):
    """Term Presentation schema for HTTP request."""

    category: list[str] | None
    marks: list[str] | None


class TermPresentationSchema(BaseSchema):
    """Term Presentation schema for HTTP response."""

    term: str
    definition: str
