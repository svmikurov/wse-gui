"""Abstract base class for Terms View."""

from abc import ABC

from wse.data.sources.glossary.term import TermNetworkSourceListenerABC
from wse.feature.base.container import CreateNavButtonABC
from wse.ui.base.abc import CloseScreenABC, NavigateABC, ViewABC


class TermsViewModelABC(
    TermNetworkSourceListenerABC,
    CloseScreenABC,
    NavigateABC,
    ABC,
):
    """ABC for Terms ViewModel."""

    def refresh_context(self) -> None:
        """Refresh screen context."""


class TermsViewABC(
    CreateNavButtonABC,
    CloseScreenABC,
    ViewABC,
    ABC,
):
    """ABC for Terms View."""
