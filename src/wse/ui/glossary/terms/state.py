"""Terms screen UI state."""

from dataclasses import dataclass

from injector import inject

from wse.core.interfaces import Navigable
from wse.feature.base.audit import AuditMixin
from wse.ui.base.mixin import NavigateStateMixin
from wse.ui.glossary.terms import TermsViewModelABC


@inject
@dataclass
class TermsViewModel(
    AuditMixin,
    NavigateStateMixin,
    TermsViewModelABC,
):
    """Terms screen ViewModel."""

    _navigator: Navigable
