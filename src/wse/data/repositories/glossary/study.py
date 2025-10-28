"""Term study Use Case."""

import logging

from injector import inject

from wse.data.sources.glossary import TermPresentationNetworkSourceABC

from . import TermPresentationRepoABC

audit = logging.getLogger('audit')


class TermPresentationRepo(TermPresentationRepoABC):
    """Term Presentation Use Case."""

    @inject
    def __init__(
        self,
        source: TermPresentationNetworkSourceABC,
    ) -> None:
        """Construt the repository."""
        self._source = source

    def get_presentation(self) -> None:
        """Get presentation."""
        audit.warning('Called `get_presentation()` of `TermPresentationRepo`')
