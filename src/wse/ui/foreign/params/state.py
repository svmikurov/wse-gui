"""Word study parameters state."""

from __future__ import annotations

import logging
from dataclasses import dataclass, fields, replace
from typing import TYPE_CHECKING, Any, override

from injector import inject

from wse.core.navigation import NavID
from wse.data.dto import foreign as dto
from wse.data.repos.foreign import (
    WordParametersRepoABC,
    WordParametersSubscriberABC,
)
from wse.data.sources import foreign as sources
from wse.feature.observer.accessor import NotifyAccessorGen
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.params import ParamsAccessorEnum

from . import WordStudyParamsViewModelABC

if TYPE_CHECKING:
    from wse.data.sources.foreign.params import WordParametersData

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class WordParametersUIState(
    dto.ParameterOptions,
    dto.SelectedParameters,
    dto.SetParameters,
    dto.PresentationSettings,
):
    """Word study parameters UIState data."""


@inject
@dataclass
class WordStudyParamsViewModel(
    NavigateStateMixin,
    ObserverManagerGen[Any],  # TODO: Update Any to ...
    NotifyAccessorGen[Any, Any],  # TODO: Update Any to ...
    sources.WordParametersNotifyABC,
    WordStudyParamsViewModelABC,
):
    """Word study parameters ViewModel."""

    _data: WordParametersUIState
    _repo: WordParametersRepoABC
    _source_subscriber: WordParametersSubscriberABC

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

    # TODO: Accessor enumeration is not completed
    # Complete or refactor?
    @override
    def update_from_widget(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update UIState data via widget."""
        self._data = replace(self._data, **{accessor: value})  # type: ignore[misc, arg-type]

    @override
    def save_params(self) -> None:
        """Save selected parameters."""
        self._repo.save(self._get_initial_params())

    @override
    def reset_params(self) -> None:
        """Reset selected parameters."""
        self._repo.refresh()

    @override
    def start_exercise(self) -> None:
        """Start exercise."""
        self._repo.set(self._get_initial_params())
        self._navigator.navigate(nav_id=NavID.FOREIGN_STUDY)

    # Notification observe
    # --------------------

    @override
    def params_updated(
        self,
        params: WordParametersData | dto.PresentationParameters,
    ) -> None:
        """Update Word study parameters."""
        self._update_state(params)
        self._provide_options()
        self._provide_options_values()

    @override
    def initial_updated(
        self,
        params: dto.InitialParameters,
    ) -> None:
        """Update Word study initial parameters."""
        self._update_state(params)
        self._provide_options_values()

    # Helpers
    # -------

    def _get_initial_params(self) -> dto.InitialParameters:
        return dto.InitialParameters.from_dto(self._data)

    def _set_initial_params(self, dto: dto.InitialParameters) -> None:
        self._data = replace(self._data, **vars(dto))

    def _update_state(
        self,
        params: WordParametersData
        | dto.PresentationParameters
        | dto.InitialParameters,
    ) -> None:
        """Update UIState data."""
        self._data = replace(self._data, **vars(params))

    def _provide_options(self) -> None:
        for accessor, options in self.accessor_options:
            self.notify('values_updated', accessor, values=options)

    def _provide_options_values(self) -> None:
        for field in fields(dto.InitialParameters):
            value = getattr(self._data, field.name, None)
            self.notify('value_updated', accessor=field.name, value=value)

    @property
    def accessor_options(self) -> tuple[tuple[str, Any], ...]:
        """Get accessor options."""
        return (
            ('category', self._data.categories),
            ('mark', self._data.marks),
            ('word_source', self._data.sources),
            ('start_period', self._data.periods),
            ('end_period', self._data.periods),
            ('translation_order', self._data.translation_orders),
        )
