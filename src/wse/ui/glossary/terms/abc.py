"""Abstract base class for Terms View."""

from abc import ABC

from wse.feature.base import ViewABC
from wse.feature.base.container import CreateNavButtonABC
from wse.ui.base.abc import CloseScreenABC, NavigateABC


class TermsViewModelABC(
    NavigateABC,
    ABC,
):
    """ABC for Terms ViewModel."""


class TermsViewABC(
    CloseScreenABC,
    CreateNavButtonABC,
    ViewABC,
    ABC,
):
    """ABC for Terms View."""
