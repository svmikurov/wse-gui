"""Index Glossary discipline screen UI state."""

import logging
from dataclasses import dataclass

from injector import inject

from wse.core.interfaces import Navigable
from wse.feature.audit import AuditMixin

from ...base.navigate.mixin import NavigateStateMixin
from . import IndexGlossaryViewModelABC

audit = logging.getLogger('audit')


@inject
@dataclass
class IndexGlossaryViewModel(
    AuditMixin,
    NavigateStateMixin,
    IndexGlossaryViewModelABC,
):
    """Index Glossary screen ViewModel."""

    _navigator: Navigable

    def refresh_content(self) -> None:
        """Refresh screen content."""
        audit.debug(f'Not implemented `refresh_content` in {self.__class__}')
