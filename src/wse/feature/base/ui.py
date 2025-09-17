"""Abstract base classes for UI layer."""

from abc import ABC
from dataclasses import dataclass

from .abstract.ui_layer import ContentABC
from .mixins import SetupMixin

# Controller


@dataclass
class Controller(
    SetupMixin,
    ContentABC,
    ABC,
):
    """Abstract base class for controller."""
