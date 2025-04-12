"""Defines account page controller."""

from dataclasses import dataclass

from wse.features.base.mvc import BaseController


@dataclass
class AccountController(BaseController):
    """Account page controller."""
