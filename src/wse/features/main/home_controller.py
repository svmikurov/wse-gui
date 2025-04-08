"""Defines home page controller."""

from dataclasses import dataclass

from wse.features.shared.mvc import BaseController


@dataclass
class HomeController(BaseController):
    """Home page controller."""
