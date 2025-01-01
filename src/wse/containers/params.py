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
from wse.source.items import SourceItems
from wse.source.number_input import SourceValue
from wse.source.switch import SourceSwitch
from wse.widgets.box import BoxFlexCol, BoxFlexRow
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel, LabelParam
from wse.widgets.message import MessageMixin
from wse.widgets.number_input import NumberInputApp
from wse.widgets.selection import SelectionApp
from wse.widgets.switch import SwitchApp

ACCESSORS = ['alias', 'name']


class ParamsSources:
    """Exercise params sources."""

    def __init__(self) -> None:
        """Construct param sources."""
        super().__init__()

        # Selection sources
        self.source_category = SourceItems(ACCESSORS)
        self.source_order = SourceItems(ACCESSORS)
        self.source_period_start_date = SourceItems(ACCESSORS)
        self.source_period_end_date = SourceItems(ACCESSORS)

        # Value sources
        self.source_input_count_first = SourceValue()
        self.source_input_count_last = SourceValue()

        # Switch progress sources
        self.source_progress_study = SourceSwitch()
        self.source_progress_repeat = SourceSwitch()
        self.source_progress_examination = SourceSwitch()
        self.source_progress_know = SourceSwitch()


class ParamsLogic(MessageMixin, ParamsSources):
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
        pprint(params)

        if params:
            self.set_params(params)
            self.populate_selections()
            self.set_default_params()
        else:
            await self.show_message(
                'Соединение с сервером:',
                'Ошибка получения\nпараметров упражнения',
            )

    def set_params(self, params: dict) -> None:
        """Set exercise params for selection task."""
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

    def set_default_params(self) -> None:
        """Set default params."""
        # Selections
        self.source_category.set_value(self.default_values['category'])
        self.source_order.set_value(self.default_values['order'])
        self.source_period_start_date.set_value(self.default_values['period_start_date'])  # noqa: E501
        self.source_period_end_date.set_value(self.default_values['period_end_date'])  # noqa: E501
        # Inputs
        self.source_input_count_first.set_value(self.default_values['count_first'])  # noqa: E501
        self.source_input_count_last.set_value(self.default_values['count_last'])  # noqa: E501
        # Switches
        self.source_progress_study.set_value('S' in self.default_values['progress'])  # noqa: E501
        self.source_progress_repeat.set_value('R' in self.default_values['progress'])  # noqa: E501
        self.source_progress_examination.set_value('E' in self.default_values['progress'])  # noqa: E501
        self.source_progress_know.set_value('K' in self.default_values['progress'])  # noqa: E501

    def set_saved_params(self) -> None:
        """Set saved params."""
        # Selections
        self.source_category.set_value(self.lookup_conditions['category'])
        self.source_order.set_value(self.lookup_conditions['order'])
        self.source_period_start_date.set_value(self.lookup_conditions['period_start_date'])  # noqa: E501
        self.source_period_end_date.set_value(self.lookup_conditions['period_end_date'])  # noqa: E501
        # Inputs
        self.source_input_count_first.set_value(self.lookup_conditions['count_first'])  # noqa: E501
        self.source_input_count_last.set_value(self.lookup_conditions['count_last'])  # noqa: E501
        # Switches
        self.source_progress_study.set_value('S' in self.lookup_conditions['progress'])  # noqa: E501
        self.source_progress_repeat.set_value('R' in self.lookup_conditions['progress'])  # noqa: E501
        self.source_progress_examination.set_value('E' in self.lookup_conditions['progress'])  # noqa: E501
        self.source_progress_know.set_value('K' in self.lookup_conditions['progress'])  # noqa: E501
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
        await request_put_async(url=self.url, payload=lookup_conditions)


class ParamsWidgets(HttpPutMixin, WidgetMixin, ParamsLogic):
    """Exercise params widgets."""

    title = ''
    """The exercise page title (`str`).
    """

    def __init__(self) -> None:
        """Construct a widgets."""
        super().__init__()

        # Title
        self.label_title = TitleLabel(text=self.title)

        # Selection labels
        self.label_category = LabelParam('Категория:')
        self.label_order = LabelParam('Порядок перевода:')
        self.label_period_start_date = LabelParam('Начало периода:')
        self.label_period_end_date = LabelParam('Конец периода:')
        # NumberInput labels
        self.label_first = LabelParam('Первые:')
        self.label_last = LabelParam('Последние:')

        # fmt: off
        # Selections
        self.selection_category = SelectionApp(accessor='name', items=self.source_category)  # noqa: E501
        self.selection_order = Selection(accessor='name', items=self.source_order)  # noqa: E501
        self.selection_period_start_date = Selection(accessor='name', items=self.source_period_start_date)  # noqa: E501
        self.selection_period_end_date = Selection(accessor='name', items=self.source_period_end_date)  # noqa: E501

        # Switches of count
        self.switch_count_first = toga.Switch('', on_change=self.first_switch_handler)  # noqa: E501
        self.switch_count_last = toga.Switch('', on_change=self.last_switch_handler)  # noqa: E501

        # Switches of progress
        self.switch_study = SwitchApp('')
        self.switch_repeat = SwitchApp('')
        self.switch_examination = SwitchApp('')
        self.switch_know = SwitchApp('')
        # Switches ara listeners.
        self.source_progress_study.add_listener(self.switch_study)
        self.source_progress_repeat.add_listener(self.switch_repeat)
        self.source_progress_examination.add_listener(self.switch_examination)
        self.source_progress_know.add_listener(self.switch_know)

        # NumberInputs
        self.input_count_first = NumberInputApp(step=10, min=0, on_change=self.source_input_count_first.update_value)  # noqa: E501
        self.input_count_last = NumberInputApp(step=10, min=0, on_change=self.source_input_count_last.update_value)  # noqa: E501
        # NumberInputs ara listeners.
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
        self.set_saved_params()

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
        self.include_selections_to_boxes()
        self.include_number_inputs_to_boxes()
        self.include_progress_switches_to_boxes()

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
        # Progress switchers
        self.box_params.add(
            self.box_progress_switchers_line1,
            self.box_progress_switchers_line2,
        )
        # Buttons
        self.box_params_btns.add(
            self.btn_goto_exercise,
            self.btn_set_saved_params,
            self.btn_reset_params,
            self.btn_save_params,
            self.btn_goto_back,
        )

    def include_selections_to_boxes(self) -> None:
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

    def include_number_inputs_to_boxes(self) -> None:
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

    def include_progress_switches_to_boxes(self) -> None:
        """Create the box-container for progress switchers."""
        self.box_progress_switchers_line1 = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Изучаю')]),
                        BoxFlexRow(children=[self.switch_study]),
                    ]
                ),
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Повторяю')]),
                        BoxFlexRow(children=[self.switch_repeat]),
                    ]
                ),
            ]
        )
        self.box_progress_switchers_line2 = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Проверяю')]),
                        BoxFlexRow(children=[self.switch_examination]),
                    ]
                ),
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Знаю')]),
                        BoxFlexRow(children=[self.switch_know]),
                    ]
                ),
            ]
        )
