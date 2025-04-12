"""Defines login page controller."""

from dataclasses import dataclass

from wse.features.base import mvc


@dataclass
class LoginController(mvc.BaseContextController):
    """Login page controller."""
