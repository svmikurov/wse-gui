"""Terms Use Cases."""

from injector import inject

from wse.data.sources.glossary import TermNetworkSourceABC

from . import GetTermsUseCaseABC


class GetTermsUseCase(GetTermsUseCaseABC):
    """Get Terms Use Case."""

    @inject
    def __init__(self, terms_network_source: TermNetworkSourceABC) -> None:
        """Construct the case."""
        self._terms_network_source = terms_network_source

    def get_terms(self) -> None:
        """Get terms."""
        self._terms_network_source.get_terms()
