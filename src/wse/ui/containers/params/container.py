"""Container for a set of parameters."""

from dataclasses import dataclass
from functools import partial
from typing import Any, override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.observer.accessor import AccessorMixin
from wse.feature.observer.mixins import AddNotifyMixin, ObserverManagerGen
from wse.ui.base.content.mixins import GetContentMixin
from wse.utils.contextmanager import EventDisabler
from wse.utils.i18n import I18N

from . import ParamsContainerABC
from .entity import IdNameSource

UI_MARGIN = (2, 5, 2, 5)


@inject
@dataclass
class ParamsContainer(
    AccessorMixin,
    AddNotifyMixin,
    ObserverManagerGen[Any],
    GetContentMixin,
    ParamsContainerABC,
):
    """Params container.

    To create Selection widget use ``_create_selection`` method.
    """

    _accessors = (
        'category',
        'mark',
        'word_source',
        'translation_order',
        'start_period',
        'end_period',
        'word_count',
        'question_timeout',
        'answer_timeout',
    )

    @override
    def _create_ui(self) -> None:
        # Selections with label
        self._category_label = toga.Label(I18N.LABEL('Category'))
        self._category = self._create_selection('category')
        self._mark_label = toga.Label(I18N.LABEL('Mark'))
        self._mark = self._create_selection('mark')
        self._word_source_label = toga.Label(I18N.LABEL('Source'))
        self._word_source = self._create_selection('word_source')
        self._translation_order_label = toga.Label(
            I18N.LABEL('Translate order')
        )
        self._translation_order = self._create_selection('translation_order')
        self._period_label = toga.Label(I18N.LABEL('Word adding period'))
        self._start_period = self._create_selection('start_period')
        self._end_period = self._create_selection('end_period')

        # Number inputs with label
        self._word_count_label = toga.Label(I18N.LABEL('Word study count'))
        self._word_count = self._create_number_input('word_count')
        self._question_timeout_label = toga.Label('')
        self._question_timeout_label.text = I18N.LABEL('Question timeout')
        self._question_timeout = self._create_number_input('question_timeout')
        self._answer_timeout_label = toga.Label(I18N.LABEL('Answer timeout'))
        self._answer_timeout = self._create_number_input('answer_timeout')

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self.select_category,
            self.select_mark,
            self.source_select,
            self.order_select,
            self.period_select,
            self.input_count,
            self.question_timeout,
            self.answer_timeout,
        )

    @override
    def _update_style(self, config: StyleConfig | ThemeConfig) -> None:
        # Selections
        self._category_label.style.update(**config.params.label)
        self._category.style.update(**config.params.select)
        self._mark_label.style.update(**config.params.label)
        self._mark.style.update(**config.params.select)
        self._word_source_label.style.update(**config.params.label)
        self._word_source.style.update(**config.params.select)
        self._translation_order_label.style.update(**config.params.label)
        self._translation_order.style.update(**config.params.select)
        self._period_label.style.update(**config.params.label)
        self._start_period.style.update(**config.params.select)
        self._end_period.style.update(**config.params.select)

        # Number input
        self._word_count_label.style.update(**config.params.label)
        self._word_count.style.update(**config.params.number)
        self._question_timeout_label.style.update(**config.params.label)
        self._question_timeout.style.update(**config.params.number)
        self._answer_timeout_label.style.update(**config.params.label)
        self._answer_timeout.style.update(**config.params.number)

    # Combined widgets
    # ----------------

    @property
    def select_category(self) -> toga.Box:
        """Get the named selection widget of category."""
        return self._combine(self._category_label, self._category)

    @property
    def select_mark(self) -> toga.Box:
        """Get the named selection widget of mark."""
        return self._combine(self._mark_label, self._mark)

    @property
    def source_select(self) -> toga.Box:
        """Get the named selection widget of source."""
        return self._combine(self._word_source_label, self._word_source)

    @property
    def order_select(self) -> toga.Box:
        """Get the named selection widget of translation order."""
        return self._combine(
            self._translation_order_label, self._translation_order
        )

    @property
    def period_select(self) -> toga.Box:
        """Get the named selection widget of period select."""
        label_row = toga.Box(margin=(10, 0, 10, 0))
        left_box = toga.Box(flex=1, margin_right=1)
        right_box = toga.Box(flex=1, margin_right=1)

        label_row.add(self._period_label)
        left_box.add(self._start_period)
        right_box.add(self._end_period)

        return toga.Column(  # type: ignore[no-any-return, no-untyped-call]
            children=[label_row, toga.Box(children=[left_box, right_box])],
            margin=UI_MARGIN,
        )

    @property
    def input_count(self) -> toga.Box:
        """Get the named input widget of word count."""
        return self._combine(self._word_count_label, self._word_count)

    @property
    def question_timeout(self) -> toga.Box:
        """Get the named input widget of question timeout."""
        return self._combine(
            self._question_timeout_label, self._question_timeout
        )

    @property
    def answer_timeout(self) -> toga.Box:
        """Get the named input widget of answer timeout."""
        return self._combine(self._answer_timeout_label, self._answer_timeout)

    # Utility methods
    # ---------------

    @staticmethod
    def _combine(label: toga.Label, widget: toga.Widget) -> toga.Box:
        """Combine into a labeled widget."""
        return toga.Box(
            children=[
                toga.Box(children=[label], flex=1),
                toga.Box(children=[widget], flex=1),
            ],
            margin=UI_MARGIN,
            align_items='center',
            flex=1,
        )

    def _create_selection(self, accessor: str) -> toga.Selection:
        """Create Selection with valid accessor."""
        self._validate_accessor(accessor)
        return toga.Selection(
            accessor='name',
            items=IdNameSource(),
            on_change=partial(self._on_select, accessor=accessor),
        )

    def _create_number_input(
        self, accessor: str, **kwargs: object
    ) -> toga.NumberInput:
        """Create number input widget."""
        self._validate_accessor(accessor)
        return toga.NumberInput(
            min=0,
            on_change=partial(self._on_change, accessor=accessor),
        )

    def _validate_accessor(self, accessor: str) -> None:
        if accessor not in self._accessors:
            raise RuntimeError(
                f"Got invalid accessor name: '{accessor}'. "
                f'Available: {self._accessors}'
            )

    # Widget callback
    # ---------------

    def _on_select(self, selection: toga.Selection, accessor: str) -> None:
        self.notify('widget_updated', accessor=accessor, value=selection.value)

    def _on_change(self, input: toga.NumberInput, accessor: str) -> None:
        self.notify('widget_updated', accessor=accessor, value=input.value)

    # Api contract
    # ------------

    @override
    def set_values(self, accessor: str, values: object) -> None:
        """Set widget values via accessor.

        Updated widget must implement ``items.update()`` Source
        interface.
        """
        ui = self._get_ui(accessor)
        with EventDisabler(ui):
            ui.items.update(values)

    @override
    def set_value(self, accessor: str, value: object) -> None:
        """Set widget value via accessor."""
        ui = self._get_ui(accessor)
        with EventDisabler(ui):
            ui.value = value
