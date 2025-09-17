"""Abstract Base Classes to subscribe Glossary discipline observers."""

from injector import Inject
from typing_extensions import override

from wse.data.sources import TermNetworkSource
from wse.data.sources.glossary.term import TermNetworkSourceListenerABC

from . import SubscribeTermsUseCaseABC


class SubscribeTermsUseCase(SubscribeTermsUseCaseABC):
    """Subscribe listener on Terms source notifications."""

    def __init__(self, source: Inject[TermNetworkSource]) -> None:
        """Construct the case."""
        self._source = source

    @override
    def add_listener(self, listener: TermNetworkSourceListenerABC) -> None:
        """Add a new listener to this data source."""
        self._source.add_listener(listener)

    @override
    def remove_listener(self, listener: TermNetworkSourceListenerABC) -> None:
        """Remove a listener from this data source."""
        self._source.remove_listener(listener)
