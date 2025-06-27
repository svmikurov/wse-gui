"""Defines Authentication page interfaces."""

from typing import Protocol

from wse.features.interfaces import IPageController, IView


class IAuthView(
    IView,
    Protocol,
):
    """Protocol for Authentication page view interface."""


class IAuthController(
    IPageController,
    Protocol,
):
    """Protocol for Authentication page controller interface."""
