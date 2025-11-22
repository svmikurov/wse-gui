"""Word study params state."""

import logging
from dataclasses import dataclass, fields, replace
from decimal import Decimal
from typing import Any, override

from injector import inject

from wse.api.foreign import requests
from wse.data.repos.foreign import WordParamsMapperABC, WordParamsRepoABC
from wse.data.sources.foreign import WordParamsNotifyABC
from wse.feature.observer.accessor import NotifyAccessorGen
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.params import ParamsAccessorEnum
from wse.utils import decorators

from . import WordStudyParamsViewModelABC

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class ParamsValue:
    """Current Presentation params values.

    Field name according widget attr name.
    """

    # Choice
    category: requests.IdName | None = None
    mark: requests.IdName | None = None
    word_source: requests.IdName | None = None
    order: requests.IdName | None = None
    start_period: requests.IdName | None = None
    end_period: requests.IdName | None = None

    # Input
    # TODO: Where update `Decimal` to `int`?
    word_count: Decimal | None = None
    question_timeout: Decimal | None = None
    answer_timeout: Decimal | None = None


@dataclass(frozen=True)
class PresentationParamsData(ParamsValue):
    """Word study Presentation data."""

    # Choices
    categories: list[requests.IdName] | None = None
    marks: list[requests.IdName] | None = None
    sources: list[requests.IdName] | None = None
    orders: list[requests.IdName] | None = None
    start_periods: list[requests.IdName] | None = None
    end_periods: list[requests.IdName] | None = None


@inject
@dataclass
class WordStudyParamsViewModel(
    NavigateStateMixin,
    ObserverManagerGen[Any],  # TODO: Update Any to ...
    NotifyAccessorGen[Any, Any],  # TODO: Update Any to ...
    WordParamsNotifyABC,
    WordStudyParamsViewModelABC,
):
    """Word study params ViewModel."""

    _data: PresentationParamsData
    _repo: WordParamsRepoABC
    _source_subscriber: WordParamsMapperABC

    @override
    def on_open(self) -> None:
        """Call methods on screen open."""
        self._source_subscriber.subscribe(self)
        self._refresh_initial_params()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._source_subscriber.unsubscribe(self)

    @decorators.log_unimplemented_call
    @override
    def start_exercise(self) -> None:
        """Start exercise."""

    # View api contract
    # -----------------

    @override
    def update_widget_state(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update widget context."""
        self._data = replace(self._data, **{accessor: value})  # type: ignore[misc, arg-type]

    @override
    def save_params(self) -> None:
        """Save selected params."""
        self._save_params()

    @override
    def reset_params(self) -> None:
        """Reset selected params."""
        self._reset_params()

    # Notification observe
    # --------------------

    @override
    def initial_params_updated(
        self,
        params: requests.PresentationParamsDTO,
    ) -> None:
        """Set Initial Word study params."""
        self._data = replace(
            self._data, **{k: v for k, v in params.__dict__.items()}
        )

        self._update('mark', 'marks')
        self._update('category', 'categories')
        self._update('word_source', 'sources')

    # Helpers
    # -------

    def _refresh_initial_params(self) -> None:
        """Refresh Initial params of Word study."""
        self._repo.fetch_params()

    # TODO: Add literal types
    def _update(self, accessor: str, values_name: str | None = None) -> None:
        """Update UI context."""
        if values_name:
            # Selection values updated
            try:
                values = getattr(self._data, values_name)
            except Exception:
                log.exception('Update UI context error')
                return
            self.notify('values_updated', accessor, values=values)

        if value := getattr(self._data, accessor, None):
            # Value updated
            self.notify('value_updated', accessor, value=value)

    def _save_params(self) -> None:
        params = self._get_current_params()
        self._repo.update_params(params)

    @decorators.log_unimplemented_call
    def _reset_params(self) -> None: ...

    def _get_current_params(self) -> requests.InitialParams:
        fields_to_update = [
            field.name for field in fields(requests.InitialParams)
        ]
        return requests.InitialParams(
            **{field: getattr(self._data, field) for field in fields_to_update}
        )
