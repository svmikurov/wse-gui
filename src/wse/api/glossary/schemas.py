"""Glossary HTTP response schemas."""

from datetime import datetime

from wse.data.schemas import base as base_schemas


class Term(base_schemas.BaseSchema):
    """Term entity."""

    id: str
    name: str
    definition: str
    created_at: datetime


class TermsData(base_schemas.ItemsData):
    """Terms data schema."""

    results: list[Term]


class TermParameters(base_schemas.BaseSchema):
    """Term Presentation schema for HTTP request."""

    category: list[str] | None
    marks: list[str] | None


class TermPresentation(base_schemas.BaseSchema):
    """Term Presentation schema for HTTP response."""

    term: str
    definition: str
