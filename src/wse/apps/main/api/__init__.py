"""Contains Core app API for http requests."""

__all__ = [
    # Schema
    'Assigned',
    'ExerciseInfo',
    # Protocol
    'AssignationsApiProto',
    'AssignedApiProto',
]

from .protocol import (
    AssignationsApiProto,
    AssignedApiProto,
)
from .schema import (
    Assigned,
    ExerciseInfo,
)
