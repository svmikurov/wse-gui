"""Glossary HTTP response schemas."""

from wse.core.api.response import Response

from .schemas import TermPresentationSchema, TermsData


class TermsResponse(Response):
    """Terms http response schema."""

    data: TermsData


class TermPresentationResponse(Response):
    """Term Presentation response schema."""

    data: TermPresentationSchema
