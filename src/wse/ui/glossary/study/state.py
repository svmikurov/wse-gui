"""Terms study UI state."""

from dataclasses import dataclass

from injector import inject

from wse.feature.base.audit import AuditMixin
from wse.ui.base.mixin import NavigateStateMixin

from . import TermsStudyViewModelABC


@inject
@dataclass
class TermsStudyViewModel(
    AuditMixin,
    NavigateStateMixin,
    TermsStudyViewModelABC,
):
    """Terms study ViewModel."""
