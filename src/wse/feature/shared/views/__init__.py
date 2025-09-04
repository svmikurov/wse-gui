"""Contains general views."""

__all__ = [
    # Shared views
    'IntegerView',
    # Shared views protocols
    'IntegerViewProto',
]

from .integer.protocol import IntegerViewProto
from .integer.view import IntegerView
