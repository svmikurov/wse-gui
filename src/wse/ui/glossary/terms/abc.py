"""Abstract base class for Terms View."""

from abc import ABC

from wse.data.sources.glossary.term import TermNetworkSourceListenerABC
from wse.ui.base.abc.navigate import CreateNavButtonABC, NavigateABC
from wse.ui.base.abc.utils import OnCloseABC
from wse.ui.base.abc.view import ViewABC


class TermsViewModelABC(
    TermNetworkSourceListenerABC,
    OnCloseABC,
    NavigateABC,
    ABC,
):
    """ABC for Terms ViewModel."""

    def refresh_context(self) -> None:
        """Refresh screen context."""


class TermsViewABC(
    CreateNavButtonABC,
    OnCloseABC,
    ViewABC,
    ABC,
):
    """ABC for Terms View."""
