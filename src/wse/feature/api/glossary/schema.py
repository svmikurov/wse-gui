"""Glossary HTTP response schemas."""

from datetime import datetime

from wse.core.api.response import ItemsData, Response
from wse.feature.base import BaseSchema


class TermSchema(BaseSchema):
    """Term entity."""

    id: str
    name: str
    definition: str
    created_at: datetime


class TermsData(ItemsData):
    """Terms data schema."""

    results: list[TermSchema]


class TermsResponse(Response):
    """Terms http response schema."""

    data: TermsData
