"""Abstract Base Classes for Terms study screen."""

from abc import ABC, abstractmethod

from wse.data.sources.base.abc import SourceABC
from wse.ui.base.abc.navigate import NavigateABC
from wse.ui.base.abc.view import ViewABC
from wse.ui.containers.presentation import (
    PresentationListenerABC,
    PresentationNotifyT,
)


class TermsStudyViewModelABC(
    SourceABC[PresentationListenerABC, PresentationNotifyT],
    NavigateABC,
    ABC,
):
    """ABC for Terms study ViewModel."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh UI context."""


class TermsStudyViewABC(
    ViewABC,
    ABC,
):
    """ABC for Terms study View."""
