"""Terms study UI state."""

from dataclasses import dataclass

from injector import inject

from wse.data.sources.base.source import SourceGen
from wse.ui.base.mixin import NavigateStateMixin
from wse.ui.containers.presentation import (
    PresentationListenerABC,
    PresentationNotifyT,
)

from . import TermsStudyViewModelABC


@inject
@dataclass
class TermsStudyViewModel(
    NavigateStateMixin,
    SourceGen[PresentationListenerABC, PresentationNotifyT],
    TermsStudyViewModelABC,
):
    """Terms study ViewModel."""

    def refresh_context(self) -> None:
        """Refresh UI context."""
        self.notify('change_case', value='Case!\nCase!')
        self.notify('change_text', value='Text!\nText\nText!')
