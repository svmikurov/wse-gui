"""Exercise params."""

from http import HTTPStatus
from pprint import pprint

import toga
from toga import Selection
from toga.style import Pack

from wse.contrib.http_requests import (
    HttpPutMixin,
    request_get,
    request_put_async,
)
from wse.handlers.goto_handler import goto_back_handler
from wse.source.number_input import SourceValue
from wse.source.params import SourceItems
from wse.widgets.box import BoxFlexCol, BoxFlexRow
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel
from wse.widgets.message import MessageMixin
from wse.widgets.number_input import NumberInputApp

ACCESSORS = ['alias', 'name']


class Params(MessageMixin):
    """Exercise params logic."""

    url = ''
    """Url to get exercise params with GET method and to save
    user lookup conditions with PUT method (`str`).
    """

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self.exercise_choices: dict | None = None
        self.default_values: dict | None = None
        self.lookup_conditions: dict | None = None

        # Sources
        self.source_category = SourceItems(ACCESSORS)
        self.source_order = SourceItems(ACCESSORS)
        self.source_period_start_date = SourceItems(ACCESSORS)
        self.source_period_end_date = SourceItems(ACCESSORS)
        self.source_input_count_first = SourceValue()
        self.source_input_count_last = SourceValue()

    async def on_open(self, _: toga.Widget) -> None:
        """Request exercise params and populate selections."""
        if not self.exercise_choices:
            await self.update_params()

    async def update_params(self) -> None:
        """Request exercise params from server.

        If the parameters are received, then populate a selections
        and set default selection values.
        """
        params = self.request_params()

        if params:
            self.set_params(params)
            self.populate_selections()
            self.set_default_selection_values()
        else:
            await self.show_message(
                'Соединение с сервером:',
                'Ошибка получения\nпараметров упражнения',
            )

    def set_params(self, params: dict) -> None:
        """Set exercise params for selection task."""
        pprint(params)
        self.exercise_choices = params['exercise_choices']
        self.default_values = params['default_values']
        self.lookup_conditions = params['lookup_conditions']

    # fmt: off
    def populate_selections(self) -> None:
        """Populate selections."""
        self.source_category.update_data(self.exercise_choices['categories'])
        self.source_order.update_data(self.exercise_choices['orders'])
        self.source_period_start_date.update_data(self.exercise_choices['edge_period_items'])  # noqa: E501
        self.source_period_end_date.update_data(self.exercise_choices['edge_period_items'])  # noqa: E501

    def set_default_selection_values(self) -> None:
        """Set default selection values."""
        self.source_category.set_value(self.default_values['category'])
        self.source_order.set_value(self.default_values['order'])
        self.source_period_start_date.set_value(self.default_values['period_start_date'])  # noqa: E501
        self.source_period_end_date.set_value(self.default_values['period_end_date'])  # noqa: E501
        self.source_input_count_first.set_value(self.default_values['count_first'])  # noqa: E501
        self.source_input_count_last.set_value(self.default_values['count_last'])  # noqa: E501


    def set_saved_selection_values(self) -> None:
        """Set saved selection values."""
        self.source_category.set_value(self.lookup_conditions['category'])
        self.source_order.set_value(self.lookup_conditions['order'])
        self.source_period_start_date.set_value(self.lookup_conditions['period_start_date'])  # noqa: E501
        self.source_period_end_date.set_value(self.lookup_conditions['period_end_date'])  # noqa: E501
        self.source_input_count_first.set_value(self.lookup_conditions['count_first'])  # noqa: E501
        self.source_input_count_last.set_value(self.lookup_conditions['count_last'])  # noqa: E501
    # fmt: on

    ####################################################################
    # HTTP requests

    def request_params(self) -> dict | None:
        """Request a exercise params."""
        response = request_get(self.url)
        if response.status_code == HTTPStatus.OK:
            return response.json()

    async def request_save_lookup_conditions(self) -> None:
        """Request to save user lookup conditions."""
        lookup_conditions = {
            'category': self.source_category.value.alias,
            'order': self.source_order.value.alias,
            'period_start_date': self.source_period_start_date.value.alias,
            'period_end_date': self.source_period_end_date.value.alias,
            'count_first': self.source_input_count_first.get_value(),
            'count_last': self.source_input_count_last.get_value(),
        }
        print(f'>>> {lookup_conditions = }')
        await request_put_async(url=self.url, payload=lookup_conditions)


class LabelParam(toga.Label):
    """Styled label of parameter."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the style of label."""
        super().__init__(*args, **kwargs)
        self.style.padding = (7, 0, 7, 2)


class ParamsWidgets(HttpPutMixin, WidgetMixin, Params):
    """Exercise params widgets."""

    title = ''
    """The exercise page title (`str`).
    """

    def __init__(self) -> None:
        """Construct a widgets."""
        super().__init__()

        # Title
        self.label_title = TitleLabel(text=self.title)

        # Labels selections
        self.label_category = LabelParam('Категория:')
        self.label_order = LabelParam('Порядок перевода:')
        self.label_period_start_date = LabelParam('Начало периода:')
        self.label_period_end_date = LabelParam('Конец периода:')
        # Labels NumberInput
        self.label_first = LabelParam('Первые:')
        self.label_last = LabelParam('Последние:')

        # fmt: off
        # Selections
        self.selection_category = Selection(accessor='name', items=self.source_category)  # noqa: E501
        self.selection_order = Selection(accessor='name', items=self.source_order)  # noqa: E501
        self.selection_period_start_date = Selection(accessor='name', items=self.source_period_start_date)  # noqa: E501
        self.selection_period_end_date = Selection(accessor='name', items=self.source_period_end_date)  # noqa: E501

        # Switches
        self.switch_count_first = toga.Switch('', on_change=self.first_switch_handler)  # noqa: E501
        self.switch_count_last = toga.Switch('', on_change=self.last_switch_handler)  # noqa: E501

        # NumberInputs
        self.input_count_first = NumberInputApp(step=10, min=0, on_change=self.source_input_count_first.update_value)
        self.input_count_last = NumberInputApp(step=10, min=0, on_change=self.source_input_count_last.update_value)
        self.source_input_count_first.add_listener(self.input_count_first)
        self.source_input_count_last.add_listener(self.input_count_last)

        # Buttons
        self.btn_goto_exercise = BtnApp('Начать упражнение', on_press=self.start_exercise_handler)  # noqa: E501
        self.btn_set_saved_params = BtnApp('Сохраненный выбор', on_press=self.set_saved_params_handler)  # noqa: E501
        self.btn_reset_params = BtnApp('Сбросить выбор', on_press=self.reset_params_handler)  # noqa: E501
        self.btn_save_params = BtnApp('Сохранить выбор', on_press=self.save_params_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)  # noqa: E501
        # fmt: on

    ####################################################################
    # Button handlers

    def start_exercise_handler(self, _: toga.Widget) -> None:
        """Start exercise, button handler."""
        pass

    def set_saved_params_handler(self, _: toga.Widget) -> None:
        """Set saved params choice, button handler."""
        self.set_saved_selection_values()

    async def reset_params_handler(self, _: toga.Widget) -> None:
        """Populate widgets by default params, button handler."""
        await self.update_params()

    async def save_params_handler(self, _: toga.Widget) -> None:
        """Save selected params, button handler."""
        await self.request_save_lookup_conditions()

    ####################################################################
    # Switch handlers

    def first_switch_handler(self, widget: toga.Widget) -> None:
        """Count of first added items, switch handler."""
        if self.switch_count_first.value:
            self.switch_count_last.value = False

    def last_switch_handler(self, widget: toga.Widget) -> None:
        """Count of last added items, switch handler."""
        if self.switch_count_last.value:
            self.switch_count_first.value = False


class ParamsLayout(ParamsWidgets, BaseBox):
    """Exercise params layout."""

    def __init__(self) -> None:
        """Construct the layout."""
        super().__init__()

        # Styles
        self.style_box_selection = Pack(padding=(2, 0, 2, 0))

        # Exercise params widgets are enclosed in boxes.
        self.include_selections_in_boxes()
        self.include_number_inputs_in_boxes()

        # Exercise parameter boxes are enclosed in ``box_params``.
        self.box_params = BoxFlexCol()

        # Exercise params buttons are enclosed in ``box_params_btns``.
        self.box_params_btns = BoxFlexCol()

        # DOM
        self.add(
            self.label_title,
            self.box_params,
            self.box_params_btns,
        )
        # Selections
        self.box_params.add(
            self.box_selection_category,
            self.box_selection_order,
            self.box_selection_period_start_date,
            self.box_selection_period_end_date,
        )
        # NumberInputs
        self.box_params.add(
            self.box_nuber_input_first,
            self.box_nuber_input_last,
        )
        # Buttons
        self.box_params_btns.add(
            self.btn_goto_exercise,
            self.btn_set_saved_params,
            self.btn_reset_params,
            self.btn_save_params,
            self.btn_goto_back,
        )

    def include_selections_in_boxes(self) -> None:
        """Construct a selection boxes."""
        self.box_selection_category = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[self.label_category]),
                BoxFlexCol(children=[self.selection_category]),
            ],
        )
        self.box_selection_order = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[self.label_order]),
                BoxFlexCol(children=[self.selection_order]),
            ],
        )
        self.box_selection_period_start_date = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[self.label_period_start_date]),
                BoxFlexCol(children=[self.selection_period_start_date]),
            ],
        )
        self.box_selection_period_end_date = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[self.label_period_end_date]),
                BoxFlexCol(children=[self.selection_period_end_date]),
            ],
        )

    def include_number_inputs_in_boxes(self) -> None:
        """Create number input boxes."""
        self.box_nuber_input_first = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[self.label_first]),
                        BoxFlexRow(children=[self.switch_count_first]),
                    ],
                ),
                BoxFlexCol(children=[self.input_count_first]),
            ]
        )
        self.box_nuber_input_last = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[self.label_last]),
                        BoxFlexRow(children=[self.switch_count_last]),
                    ],
                ),
                BoxFlexCol(children=[self.input_count_last]),
            ]
        )
