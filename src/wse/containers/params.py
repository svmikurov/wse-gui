"""Exercise params."""

from http import HTTPStatus

import toga
from toga import Selection
from toga.style import Pack

from wse.contrib.http_requests import (
    HttpPutMixin,
    request_get,
    request_put_async,
)
from wse.handlers.goto_handler import goto_back_handler
from wse.source.number_input import SourceDecimal
from wse.source.selection import SourceSelections
from wse.source.switch import SourceSwitch
from wse.widgets.box import BoxFlexCol, BoxFlexRow
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import LabelParam, TitleLabel
from wse.widgets.message import MessageMixin
from wse.widgets.number_input import NumberInputApp
from wse.widgets.switch import SwitchApp

ACCESSORS = ['alias', 'name']


class ParamsSources:
    """Exercise params sources."""

    def __init__(self) -> None:
        """Construct param sources."""
        super().__init__()

        # Selection sources
        self.category = SourceSelections(ACCESSORS)
        self.source = SourceSelections(ACCESSORS)
        self.order = SourceSelections(ACCESSORS)
        self.period_start_date = SourceSelections(ACCESSORS)
        self.period_end_date = SourceSelections(ACCESSORS)

        # Decimal sources
        self.count_first = SourceDecimal()
        self.count_last = SourceDecimal()
        self.timeout = SourceDecimal()

        # Switches first or last, timeout
        self.is_first = SourceSwitch()
        self.is_last = SourceSwitch()
        self.has_timeout = SourceSwitch()

        # Switch progress sources
        self.progress_study = SourceSwitch()
        self.progress_repeat = SourceSwitch()
        self.progress_examination = SourceSwitch()
        self.progress_know = SourceSwitch()

        # Switch favorites
        self.favorites = SourceSwitch()


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
        """Set exercise params for selection task as attr."""
        self.exercise_choices = params['exercise_choices']
        self.default_values = params['default_values']
        self.lookup_conditions = params['lookup_conditions']

    # fmt: off
    def populate_selections(self) -> None:
        """Populate the selections with the choices."""
        # Only selections has choices.
        self.category.update_data(self.exercise_choices['categories'])
        self.source.update_data(self.exercise_choices['source'])
        self.order.update_data(self.exercise_choices['orders'])
        self.period_start_date.update_data(self.exercise_choices['edge_period_items'])  # noqa: E501
        self.period_end_date.update_data(self.exercise_choices['edge_period_items'])  # noqa: E501

    def set_default_params(self) -> None:
        """Set default params."""
        # Selections
        self.category.set_value(self.default_values['category'])
        self.source.set_value(self.default_values['source'])
        self.order.set_value(self.default_values['order'])
        self.period_start_date.set_value(self.default_values['period_start_date'])  # noqa: E501
        self.period_end_date.set_value(self.default_values['period_end_date'])
        # Inputs
        self.is_first.set_value(self.default_values['is_first'])
        self.is_last.set_value(self.default_values['is_last'])
        self.count_first.set_value(self.default_values['count_first'])
        self.count_last.set_value(self.default_values['count_last'])
        self.has_timeout.set_value(self.default_values['has_timeout'])
        self.timeout.set_value(self.default_values['timeout'])
        # Switches
        self.progress_study.set_value('S' in self.default_values['progress'])
        self.progress_repeat.set_value('R' in self.default_values['progress'])
        self.progress_examination.set_value('E' in self.default_values['progress'])  # noqa: E501
        self.progress_know.set_value('K' in self.default_values['progress'])
        self.favorites.set_value(self.default_values['favorites'])

    def set_saved_params(self) -> None:
        """Set saved params."""
        # Selections
        self.category.set_value(self.lookup_conditions['category'])
        self.source.set_value(self.lookup_conditions['source'])
        self.order.set_value(self.lookup_conditions['order'])
        self.period_start_date.set_value(self.lookup_conditions['period_start_date'])  # noqa: E501
        self.period_end_date.set_value(self.lookup_conditions['period_end_date'])  # noqa: E501
        # Inputs
        self.is_first.set_value(self.lookup_conditions['is_first'])
        self.is_last.set_value(self.lookup_conditions['is_last'])
        self.count_first.set_value(self.lookup_conditions['count_first'])
        self.count_last.set_value(self.lookup_conditions['count_last'])
        self.has_timeout.set_value(self.lookup_conditions['has_timeout'])
        self.timeout.set_value(self.lookup_conditions['timeout'])

        # Switches
        self.progress_study.set_value('S' in self.lookup_conditions['progress'])  # noqa: E501
        self.progress_repeat.set_value('R' in self.lookup_conditions['progress'])  # noqa: E501
        self.progress_examination.set_value('E' in self.lookup_conditions['progress'])  # noqa: E501
        self.progress_know.set_value('K' in self.lookup_conditions['progress'])
        self.favorites.set_value(self.lookup_conditions['favorites'])
    # fmt: on

    def get_progress_choice(self) -> list:
        """Get progress choice using switches."""
        progress = []
        if self.progress_study.get_value():
            progress.append('S')
        if self.progress_repeat.get_value():
            progress.append('R')
        if self.progress_examination.get_value():
            progress.append('E')
        if self.progress_know.get_value():
            progress.append('K')
        return progress

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
            'category': self.category.value.alias,
            'source': self.source.value.alias,
            'count_first': self.count_first.get_value(),
            'count_last': self.count_last.get_value(),
            'favorites': self.favorites.get_value(),
            'is_first': self.is_first.get_value(),
            'is_last': self.is_last.get_value(),
            'order': self.order.value.alias,
            'period_start_date': self.period_start_date.value.alias,
            'period_end_date': self.period_end_date.value.alias,
            'progress': self.get_progress_choice(),
            'has_timeout': self.has_timeout.get_value(),
            'timeout': self.timeout.get_value(),
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

        # fmt: off
        # Selections
        self.selection_category = Selection(accessor='name', items=self.category)  # noqa: E501
        self.selection_source = Selection(accessor='name', items=self.source)  # noqa: E501
        self.selection_order = Selection(accessor='name', items=self.order)  # noqa: E501
        self.selection_period_start_date = Selection(accessor='name', items=self.period_start_date)  # noqa: E501
        self.selection_period_end_date = Selection(accessor='name', items=self.period_end_date)  # noqa: E501

        # Switches of count
        self.switch_is_first = SwitchApp(text='', on_change=self.is_first.update_value)  # noqa: E501
        self.switch_is_last = SwitchApp(text='', on_change=self.is_last.update_value)  # noqa: E501
        # Switches are listeners.
        self.is_first.add_listener(self.switch_is_first)
        self.is_last.add_listener(self.switch_is_last)
        # NumberInputs
        self.input_count_first = NumberInputApp(step=10, min=0, on_change=self.count_first.update_value)  # noqa: E501
        self.input_count_last = NumberInputApp(step=10, min=0, on_change=self.count_last.update_value)  # noqa: E501
        # NumberInputs ara listeners.
        self.count_first.add_listener(self.input_count_first)
        self.count_last.add_listener(self.input_count_last)

        # Switches of progress
        self.switch_study = SwitchApp(text='', on_change=self.progress_study.update_value)  # noqa: E501
        self.switch_repeat = SwitchApp(text='', on_change=self.progress_repeat.update_value)  # noqa: E501
        self.switch_examination = SwitchApp(text='', on_change=self.progress_examination.update_value)  # noqa: E501
        self.switch_know = SwitchApp(text='', on_change=self.progress_know.update_value)  # noqa: E501
        # Switches are listeners.
        self.progress_study.add_listener(self.switch_study)
        self.progress_repeat.add_listener(self.switch_repeat)
        self.progress_examination.add_listener(self.switch_examination)
        self.progress_know.add_listener(self.switch_know)

        # Switch of favorites
        self.switch_favorites = SwitchApp(text='', on_change=self.favorites.update_value)  # noqa: E501
        self.favorites.add_listener(self.switch_favorites)

        # Timeout
        self.switch_timeout = SwitchApp(text='', on_change=self.has_timeout.update_value)  # noqa: E501
        self.input_timeout = NumberInputApp(step=1, min=0, on_change=self.timeout.update_value)  # noqa: E501
        self.has_timeout.add_listener(self.switch_timeout)
        self.timeout.add_listener(self.input_timeout)

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
        self.include_favorites_switch_to_box()
        self.include_timeout_to_box()

        # Exercise parameter boxes are enclosed in ``box_params``.
        self.box_params = BoxFlexCol()

        # Box Params is included in scroll container.
        self.scroll_container = toga.ScrollContainer(
            style=Pack(flex=1),
            content=self.box_params,
        )

        # DOM
        self.add(
            self.label_title,
            self.scroll_container,
            self.btn_goto_exercise,
            self.btn_set_saved_params,
            self.btn_reset_params,
            self.btn_save_params,
            self.btn_goto_back,
        )
        # Selections
        self.box_params.add(
            self.box_selection_category,
            self.box_selection_source,
            self.box_selection_order,
            self.box_selection_period_start_date,
            self.box_selection_period_end_date,
        )
        # NumberInputs
        self.box_params.add(
            self.box_nuber_input_first,
            self.box_nuber_input_last,
            self.box_timeout,
        )
        # Progress switchers
        self.box_params.add(
            self.box_progress_switchers_line1,
            self.box_progress_switchers_line2,
        )
        # Favorites
        self.box_params.add(
            self.box_favorites,
        )

    def include_selections_to_boxes(self) -> None:
        """Construct a selection boxes."""
        self.box_selection_category = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Категория:')]),
                BoxFlexCol(children=[self.selection_category]),
            ],
        )
        self.box_selection_source = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Источник:')]),
                BoxFlexCol(children=[self.selection_source]),
            ],
        )
        self.box_selection_order = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Порядок перевода:')]),
                BoxFlexCol(children=[self.selection_order]),
            ],
        )
        self.box_selection_period_start_date = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Начало периода:')]),
                BoxFlexCol(children=[self.selection_period_start_date]),
            ],
        )
        self.box_selection_period_end_date = toga.Box(
            style=self.style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Конец периода:')]),
                BoxFlexCol(children=[self.selection_period_end_date]),
            ],
        )

    def include_number_inputs_to_boxes(self) -> None:
        """Create number input boxes."""
        self.box_nuber_input_first = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Первые:')]),
                        BoxFlexRow(children=[self.switch_is_first]),
                    ],
                ),
                BoxFlexCol(children=[self.input_count_first]),
            ]
        )
        self.box_nuber_input_last = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Последние:')]),
                        BoxFlexRow(children=[self.switch_is_last]),
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

    def include_favorites_switch_to_box(self) -> None:
        """Create the box-container for favorites switchers."""
        self.box_favorites = toga.Box(
            children=[
                BoxFlexRow(children=[LabelParam('Только избранное')]),
                BoxFlexRow(children=[self.switch_favorites]),
            ]
        )

    def include_timeout_to_box(self) -> None:
        """Create the box-container for timeout switchers."""
        self.box_timeout = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Таймаут:')]),
                        BoxFlexRow(children=[self.switch_timeout]),
                    ],
                ),
                BoxFlexCol(children=[self.input_timeout]),
            ]
        )
