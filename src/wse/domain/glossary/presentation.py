"""Presentation Use Case."""

from injector import inject

from wse.data.repositories.glossary import TermPresentationRepoABC

from . import TermPresentationUseCaseABC


class TermPresentationUseCase(TermPresentationUseCaseABC):
    """Presenatation Use Case."""

    @inject
    def __init__(
        self,
        repo: TermPresentationRepoABC,
    ) -> None:
        """Constrct the case."""
        self._repo = repo

    def get_presentation(self) -> None:
        """Get presentation."""
        self._repo.get_presentation()
