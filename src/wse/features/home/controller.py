"""Defines home page controller."""

from dataclasses import dataclass

from wse.features.shared.base import BaseController


@dataclass
class HomeController(BaseController):
    """Home page controller."""
