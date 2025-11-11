"""Glossary HTTP response schemas."""

from ..responses import Response
from . import schemas


class TermsResponse(Response):
    """Terms http response schema."""

    data: schemas.TermsData


class TermPresentationResponse(Response):
    """Term Presentation response schema."""

    data: schemas.TermPresentationSchema
