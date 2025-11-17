"""Params container."""

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
from .entity import NamedEntitySource

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
        'category_select',
        'label_select',
        'source_select',
        'order_select',
        'start_period_select',
        'end_period_select',
        'count_input',
        'question_timeout_input',
        'answer_timeout_input',
    )

    @override
    def _create_ui(self) -> None:
        # Selection with label
        self._category_label = toga.Label(I18N.LABEL('Category'))
        self._category_select = self._create_selection('category_select')
        self._label_label = toga.Label(I18N.LABEL('Label'))
        self._label_select = self._create_selection('label_select')
        self._source_label = toga.Label(I18N.LABEL('Source'))
        self._source_select = self._create_selection('source_select')
        self._order_label = toga.Label(I18N.LABEL('Translate order'))
        self._order_select = self._create_selection('order_select')

        self._period_label = toga.Label(I18N.LABEL('Word adding period'))
        self._start_period_select = self._create_selection(
            'start_period_select'
        )
        self._end_period_select = self._create_selection('end_period_select')

        # Number input with label
        self._count_label = toga.Label(I18N.LABEL('Word study count'))
        self._count_input = self._create_number_input('count_input')
        self._question_timeout_label = toga.Label(
            I18N.LABEL('Question timeout')
        )
        self._question_timeout_input = self._create_number_input(
            'question_timeout_input',
            # step=0.1,
        )
        self._answer_timeout_label = toga.Label(I18N.LABEL('Answer timeout'))
        self._answer_timeout_input = self._create_number_input(
            'answer_timeout_input',
            # step=0.1,
        )

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self.select_category,
            self.select_label,
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
        self._category_select.style.update(**config.params.select)
        self._label_label.style.update(**config.params.label)
        self._label_select.style.update(**config.params.select)
        self._source_label.style.update(**config.params.label)
        self._source_select.style.update(**config.params.select)
        self._order_label.style.update(**config.params.label)
        self._order_select.style.update(**config.params.select)
        self._period_label.style.update(**config.params.label)
        self._start_period_select.style.update(**config.params.select)
        self._end_period_select.style.update(**config.params.select)

        # Number input
        self._count_label.style.update(**config.params.label)
        self._count_input.style.update(**config.params.number)
        self._question_timeout_label.style.update(**config.params.label)
        self._question_timeout_input.style.update(**config.params.number)
        self._answer_timeout_label.style.update(**config.params.label)
        self._answer_timeout_input.style.update(**config.params.number)

    # Combined widgets
    # ----------------

    @property
    def select_category(self) -> toga.Box:
        """Word count select."""
        return self._combine(self._category_label, self._category_select)

    @property
    def select_label(self) -> toga.Box:
        """Label select."""
        return self._combine(self._label_label, self._label_select)

    @property
    def source_select(self) -> toga.Box:
        """Source select."""
        return self._combine(self._source_label, self._source_select)

    @property
    def order_select(self) -> toga.Box:
        """Order select."""
        return self._combine(self._order_label, self._order_select)

    @property
    def input_count(self) -> toga.Box:
        """Word count input."""
        return self._combine(self._count_label, self._count_input)

    @property
    def period_select(self) -> toga.Box:
        """Word adding period select."""
        label_row = toga.Box(margin=(10, 0, 10, 0))
        left_box = toga.Box(flex=1, margin_right=1)
        right_box = toga.Box(flex=1, margin_right=1)

        label_row.add(self._period_label)
        left_box.add(self._start_period_select)
        right_box.add(self._end_period_select)

        return toga.Column(  # type: ignore[no-any-return, no-untyped-call]
            children=[label_row, toga.Box(children=[left_box, right_box])],
            margin=UI_MARGIN,
        )

    @property
    def question_timeout(self) -> toga.Box:
        """Question timeout input."""
        return self._combine(
            self._question_timeout_label, self._question_timeout_input
        )

    @property
    def answer_timeout(self) -> toga.Box:
        """Answer timeout input."""
        return self._combine(
            self._answer_timeout_label, self._answer_timeout_input
        )

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
            items=NamedEntitySource(),
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

    # Source methods
    # --------------

    @override
    def set_values(self, accessor: str, value: object) -> None:
        """Set widget values via accessor.

        Updated widget must implement ``items.update()`` Source
        interface.
        """
        ui = self._get_ui(accessor)
        with EventDisabler(ui):
            ui.items.update(value)

    @override
    def set_value(self, accessor: str, value: object) -> None:
        """Set widget value via accessor."""
        ui = self._get_ui(accessor)
        with EventDisabler(ui):
            ui.value = value
