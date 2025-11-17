"""Word study params state."""

import logging
from dataclasses import dataclass, replace
from decimal import Decimal
from typing import Any, override

from injector import inject

from wse.api.schemas.base import IdNameSchema
from wse.data.repos.foreign import WordParamsMapperABC, WordParamsRepoABC
from wse.data.sources.foreign import WordParamsNotifyABC
from wse.data.sources.foreign.schemas import ParamsChoices
from wse.feature.observer.accessor import NotifyAccessorGen
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.params import ParamsAccessorEnum
from wse.utils import decorators

from . import WordStudyParamsViewModelABC

audit = logging.getLogger('audit')


@dataclass
class WordParamsSourceData:
    """Word study Source data.

    Field name according schemas name.
    """

    categories: list[IdNameSchema] | None = None
    labels: list[IdNameSchema] | None = None

    default_category: IdNameSchema | None = None
    default_label: IdNameSchema | None = None


# TODO: Combine source and widget data to UIState
@dataclass(frozen=True)
class WordParamsWidgetData:
    """Word study Widgets data.

    Field name according widget attr name.
    """

    category_select: IdNameSchema | None = None
    label_select: IdNameSchema | None = None
    source_select: IdNameSchema | None = None
    order_select: IdNameSchema | None = None
    start_period_select: IdNameSchema | None = None
    end_period_select: IdNameSchema | None = None

    count_input: Decimal | None = None
    question_timeout_input: Decimal | None = None
    answer_timeout_input: Decimal | None = None


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

    _source_data: WordParamsSourceData
    _widget_data: WordParamsWidgetData
    _repo: WordParamsRepoABC
    _source_mapper: WordParamsMapperABC

    @override
    def on_open(self) -> None:
        """Call methods on screen open."""
        self._source_mapper.subscribe(self)
        self._refresh_initial_params()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._source_mapper.unsubscribe(self)

    @override
    def start_exercise(self) -> None:
        """Start exercise."""
        self._update_locale_params()

    # API for View
    # ------------

    @override
    def update_widget_state(
        self,
        accessor: ParamsAccessorEnum,
        value: object,
    ) -> None:
        """Update widget context."""
        self._widget_data = replace(self._widget_data, **{accessor: value})  # type: ignore[misc, arg-type]

    # Notification observe
    # --------------------

    @override
    def initial_params_updated(self, params: ParamsChoices) -> None:
        """Set Initial Word study params."""
        self._source_data = replace(
            self._source_data, **{k: v for k, v in params}
        )

        self._update('label_select', 'labels', 'default_label')
        self._update('category_select', 'categories', 'default_category')

    # Utility methods
    # ---------------

    def _refresh_initial_params(self) -> None:
        """Refresh Initial params of Word study."""
        self._repo.refresh_initial_params()

    def _update(
        self, accessor: str, values_name: str, value_name: str | None = None
    ) -> None:
        """Update UI values and."""
        values_name = getattr(self._source_data, values_name)
        self.notify('source_updated', accessor, value=values_name)

        if value_name is not None:
            value_name = getattr(self._source_data, value_name)
            self.notify('default_updated', accessor, value=value_name)

    @decorators.log_unimplemented_call
    def _update_locale_params(self) -> None:
        """Update Word study params Locale source."""
