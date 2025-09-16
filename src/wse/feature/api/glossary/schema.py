"""Glossary HTTP response schemas."""

from wse.core.api.response import ItemsData, Response
from wse.data.entities import Term


class TermsData(ItemsData):
    """Terms data schema."""

    results: list[Term]


class TermsResponse(Response):
    """Terms http response schema."""

    data: TermsData
