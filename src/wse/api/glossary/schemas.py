"""Glossary HTTP response schemas."""

from datetime import datetime

from ..schemas import base as base_schemas


class TermSchema(base_schemas.BaseSchema):
    """Term entity."""

    id: str
    name: str
    definition: str
    created_at: datetime


class TermsData(base_schemas.ItemsData):
    """Terms data schema."""

    results: list[TermSchema]


class TermPresentationParamsSchema(base_schemas.BaseSchema):
    """Term Presentation schema for HTTP request."""

    category: list[str] | None
    marks: list[str] | None


class TermPresentationSchema(base_schemas.BaseSchema):
    """Term Presentation schema for HTTP response."""

    term: str
    definition: str
