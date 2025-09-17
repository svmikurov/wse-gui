"""Abstract base class for Terms View."""

from abc import ABC

from wse.data.sources.glossary.term import TermNetworkSourceObserverABC
from wse.feature.base import ViewABC
from wse.feature.base.container import CreateNavButtonABC
from wse.ui.base.abc import CloseScreenABC, NavigateABC


class TermsViewModelABC(
    TermNetworkSourceObserverABC,
    NavigateABC,
    ABC,
):
    """ABC for Terms ViewModel."""

    def refresh_context(self) -> None:
        """Refresh screen context."""


class TermsViewABC(
    CloseScreenABC,
    CreateNavButtonABC,
    ViewABC,
    ABC,
):
    """ABC for Terms View."""
