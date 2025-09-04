"""Defines API."""

__all__ = [
    # Schema
    'RelatedData',
    # Response schema
    'QuestionResponse',
    'ResultResponse',
    # Protocol
    'AuthAPIjwtProto',
    'ExerciseApiProto',
]

from .protocol import (
    AuthAPIjwtProto,
    ExerciseApiProto,
)
from .response import (
    QuestionResponse,
    RelatedData,
    ResultResponse,
)
