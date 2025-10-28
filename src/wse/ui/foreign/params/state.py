"""Word study params state."""

import logging
from dataclasses import dataclass, replace
from typing import Any, override

from injector import inject

from wse.data.repositories.foreign import (
    WordParamsMapperABC,
    WordParamsRepoABC,
)
from wse.data.sources.foreign import WordParamsNotifyABC
from wse.data.sources.foreign.schemas import (
    IdNameSchema,
    WordParamsSchema,
)
from wse.feature.observer.accessor import NotifyAccessorGen
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin

from . import WordStudyParamsViewModelABC

audit = logging.getLogger('audit')


@dataclass
class WordParamsSourceData:
    """Word study Source data."""

    # Field name according schemas name
    default_category: IdNameSchema | None = None
    default_label: IdNameSchema | None = None
    categories: list[IdNameSchema] | None = None
    labels: list[IdNameSchema] | None = None


@dataclass
class WordParamsWidgetData:
    """Word study Widgets data."""

    # Field name according widget attr name
    label_select: IdNameSchema | None = None
    category_select: IdNameSchema | None = None


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

    _source: WordParamsSourceData
    _widget: WordParamsWidgetData
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

    # Utility methods
    # ---------------

    def _refresh_initial_params(self) -> None:
        """Refresh Initial params of Word study."""
        self._repo.refresh_initial_params()

    def _update_locale_params(self) -> None:
        """Update Word study params Locale source."""
        audit.warning('Not implemented `_update_locale_params`')

    # Notification handlers
    # ---------------------

    # TODO: Refactor
    @override
    def initial_params_updated(self, params: WordParamsSchema) -> None:
        """Set Initial Word study params."""
        self._source = replace(
            self._source, **{k: v for k, v in params.__dict__.items()}
        )
        self.notify('update', 'label_select', value=self._source.labels)
        self.notify('update', 'category_select', value=self._source.categories)
