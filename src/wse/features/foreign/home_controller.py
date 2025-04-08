"""Defines Foreign home page controller."""

from dataclasses import dataclass

from wse.features.shared.mvc import BaseController


@dataclass
class ForeignController(BaseController):
    """Foreign home page controller."""
