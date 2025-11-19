"""Word study params state."""

from dataclasses import dataclass, fields, replace
from decimal import Decimal
from typing import Any, override

from injector import inject

from wse.api.foreign.schemas import ParamsChoices
from wse.api.schemas.base import IdNameSchema
from wse.data.repos.foreign import WordParamsMapperABC, WordParamsRepoABC
from wse.data.sources.foreign import WordParamsNotifyABC
from wse.feature.observer.accessor import NotifyAccessorGen
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.params import ParamsAccessorEnum
from wse.utils import decorators

from . import WordStudyParamsViewModelABC


@dataclass(frozen=True)
class ParamsValue:
    """Current Presentation params values.

    Field name according widget attr name.
    """

    # Choice
    category: IdNameSchema | None = None
    label: IdNameSchema | None = None
    source: IdNameSchema | None = None
    order: IdNameSchema | None = None
    start_period: IdNameSchema | None = None
    end_period: IdNameSchema | None = None

    # Input
    # TODO: Where update `Decimal` to `int`?
    count: Decimal | None = None
    question_timeout: Decimal | None = None
    answer_timeout: Decimal | None = None


@dataclass(frozen=True)
class PresentationParamsData(ParamsValue):
    """Word study Presentation data."""

    # Choices
    categories: list[IdNameSchema] | None = None
    labels: list[IdNameSchema] | None = None
    sources: list[IdNameSchema] | None = None
    orders: list[IdNameSchema] | None = None
    start_periods: list[IdNameSchema] | None = None
    end_periods: list[IdNameSchema] | None = None


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
    def initial_params_updated(self, params: ParamsChoices) -> None:
        """Set Initial Word study params."""
        self._data = replace(self._data, **{k: v for k, v in params})

        self._update('label', 'labels')
        self._update('category', 'categories')

    # Utility methods
    # ---------------

    def _refresh_initial_params(self) -> None:
        """Refresh Initial params of Word study."""
        self._repo.refresh_initial_params()

    # TODO: Add literal types
    def _update(self, accessor: str, values_name: str | None = None) -> None:
        """Update UI context."""
        if values_name:
            # Selection values updated
            values = getattr(self._data, values_name)
            self.notify('values_updated', accessor, values=values)

        if value := getattr(self._data, accessor, None):
            # Value updated
            self.notify('value_updated', accessor, value=value)

    def _save_params(self) -> None:
        params = self._get_current_params()
        self._repo.save_params(params)

    @decorators.log_unimplemented_call
    def _reset_params(self) -> None: ...

    def _get_current_params(self) -> ParamsValue:
        fields_to_update = [field.name for field in fields(ParamsValue)]
        return ParamsValue(
            **{field: getattr(self._data, field) for field in fields_to_update}
        )
