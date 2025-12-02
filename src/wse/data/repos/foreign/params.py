"""Word study params repository."""

import logging
from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.dto import foreign as dto
from wse.data.sources import foreign as sources

from . import WordParametersRepoABC, WordParametersSubscriberABC

log = logging.getLogger(__name__)


@inject
@dataclass
class WordParametersRepo(
    WordParametersRepoABC,
):
    """Word study params repository."""

    _network_source: sources.WordParametersNetworkSourceABC
    _local_source: sources.WordParametersLocaleSourceABC

    @override
    def fetch(self) -> None:
        """Fetch Word study parameters."""
        data = self._network_source.fetch()
        self._local_source.update(data)

    @override
    def get(self) -> dto.InitialParameters:
        """Get Word study initial parameters."""
        return self._local_source.get_initial()

    @override
    def get_settings(self) -> dto.PresentationSettings:
        """Get Word study presentation settings."""
        params = self.get()

        if not params.question_timeout and not params.answer_timeout:
            self.fetch()
            params = self.get()

        return dto.PresentationSettings(
            params.question_timeout, params.answer_timeout
        )

    @override
    def set(self, data: dto.InitialParameters) -> None:
        """Set Word study initial parameters."""
        return self._local_source.update(data)

    @override
    def save(self, data: dto.InitialParameters) -> None:
        """Save Word study parameters."""
        try:
            updated_data = self._network_source.save(data)
        except Exception:
            log.exception(
                'Network source of save parameters error, saved locally'
            )
            self._local_source.update(data)
        else:
            self._local_source.update(updated_data)

    @override
    def refresh(self) -> None:
        """Refresh Word study parameters."""
        self._local_source.refresh_initial()


@inject
@dataclass
class WordParametersSubscriber(WordParametersSubscriberABC):
    """Word study params Source mapper."""

    _local_params_source: sources.WordParametersLocaleSourceABC

    @override
    def subscribe(self, observer: sources.WordParametersNotifyABC) -> None:
        """Subscribe observer to Word params source notifications."""
        self._local_params_source.add_observer(observer)

    @override
    def unsubscribe(self, observer: sources.WordParametersNotifyABC) -> None:
        """Unsubscribe observer to Word params source notifications."""
        self._local_params_source.remove_observer(observer)
