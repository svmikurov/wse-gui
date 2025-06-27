"""Defines Login page component interfaces."""

from wse.features.interfaces import IPageController, IView


class ILoginView(IView):
    """Protocol for Login page view interface."""


class ILoginController(IPageController):
    """Protocol for Login page view interface."""
