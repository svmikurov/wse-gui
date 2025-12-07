"""Word study parameters UIState."""

import logging
from dataclasses import dataclass, replace
from typing import override

from injector import inject

from wse.core.navigation import NavID
from wse.data.dto import foreign as dto
from wse.data.repos import foreign as repos
from wse.data.sources import foreign as sources
from wse.feature import observer
from wse.ui.base import navigate
from wse.ui.foreign import parameters as base

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class WordParametersUIState(
    dto.PresentationParameters,
):
    """Word study parameters UIState data."""


@inject
@dataclass
class WordStudyParamsViewModel(
    navigate.NavigateStateMixin,
    observer.ObserverManagerGen[base.ParametersViewModelObserverABC],
    observer.NotifyAccessorGen[base.NotifyT, dto.ParameterAccessors],
    sources.WordParametersNotifyABC,
    base.WordStudyParamsViewModelABC,
):
    """Word study parameters ViewModel."""

    _data: WordParametersUIState
    _repo: repos.WordParametersRepoABC
    _source_subscriber: repos.WordParametersSubscriberABC

    def __post_init__(self) -> None:
        """Construct the ViewModel."""
        self._source_subscriber.subscribe(self)

    @override
    def on_open(self) -> None:
        """Call methods on screen open."""
        self._repo.fetch()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._source_subscriber.unsubscribe(self)

    # View api contract
    # -----------------

    @override
    def update_from_widget(
        self,
        accessor: dto.ParameterAccessors,
        value: str | dto.Selected | None,
    ) -> None:
        """Update UIState data via widget."""
        match value:
            case dto.NOT_SELECTED:
                new_value = None

            case _:
                new_value = value

        self._data = replace(self._data, **{accessor: new_value})  # type: ignore[misc, arg-type]

    @override
    def save_params(self) -> None:
        """Save selected parameters."""
        self._repo.save(self._data.initial)

    @override
    def reset_params(self) -> None:
        """Reset selected parameters."""
        self._repo.refresh()

    @override
    def start_exercise(self) -> None:
        """Start exercise."""
        self._repo.set(self._data.initial)
        self._navigator.navigate(nav_id=NavID.FOREIGN_STUDY)

    # Notification observe
    # --------------------

    @override
    def params_updated(
        self,
        params: dto.PresentationParameters,
    ) -> None:
        """Update Word study parameters."""
        self._update_state(params)
        self._provide_options()
        self._provide_option_value()

    @override
    def initial_updated(
        self,
        params: dto.InitialParameters,
    ) -> None:
        """Update Word study initial parameters."""
        self._update_state(params)
        self._provide_option_value()

    # Helpers
    # -------

    def _update_state(
        self,
        params: dto.PresentationParameters | dto.InitialParameters,
    ) -> None:
        """Update UIState data via DTO."""
        self._data = replace(self._data, **vars(params))

    def _provide_options(self) -> None:
        """Provide options."""
        for field, values in self._data.iterate_options():
            self.notify('values_updated', accessor=field, values=values)

    def _provide_option_value(self) -> None:
        """Provide option initial value."""
        for field, value in self._data.iterate_initial():
            self.notify('value_updated', accessor=field, value=value)
