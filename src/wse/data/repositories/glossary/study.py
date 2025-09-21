"""Term study Use Case."""

from injector import inject

from wse.data.sources.glossary import TermPresentationNetworkSourceABC

from . import TermPresentationRepoABC


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
        print('Called `get_presentation()` of `TermPresentationRepo`')
