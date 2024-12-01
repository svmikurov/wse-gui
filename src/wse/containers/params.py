"""Exercise params."""

from http import HTTPStatus

import toga
from toga import Label, NumberInput, Selection, Switch
from toga.constants import COLUMN
from toga.sources import ListSource
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin, request_get
from wse.widgets.box import FlexBox
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel

SELECTIONS = {
    'selection_category': {
        'source': 'source_category',
        'items': 'categories',
        'default': 'category',
    },
    'selection_progress': {
        'source': 'source_progress',
        'items': 'progress',
        'default': 'progress',
    },
    'selection_start_date': {
        'source': 'source_start_date',
        'items': 'edge_period_items',
        'default': 'period_start_date',
    },
    'selection_end_date': {
        'source': 'source_end_date',
        'items': 'edge_period_items',
        'default': 'period_end_date',
    },
}
"""A names of params selections and it attr value names (`dict`).
"""


class Params:
    """Exercise params."""

    url = ''
    """The exercise params url (`str`).
    """

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self.accessors = ['alias', 'name']

        # Sources.
        self.source_category = ListSource(accessors=self.accessors)
        self.source_progress = ListSource(accessors=self.accessors)
        self.source_start_date = ListSource(accessors=self.accessors)
        self.source_end_date = ListSource(accessors=self.accessors)

    async def on_open(self, _: toga.Widget) -> None:
        """Request params and update widgets when box open."""
        params = self.request_params()
        self.update_selections(params)

    def request_params(self) -> dict:
        """Request exercise params."""
        response = request_get(url=self.url)
        if response.status_code == HTTPStatus.OK:
            return response.json()

    def update_selections(self, params: dict) -> None:
        """Update an exercise param selections."""
        for selection_name, param_attr in SELECTIONS.items():
            # Get data to update.
            source_name = param_attr['source']
            items = params['exercise_choices'][param_attr['items']]
            default = params['lookup_conditions'][param_attr['default']]

            self.update_selection(items, default, source_name, selection_name)

    def update_selection(
        self,
        items: dict,
        default: str | int | None,
        source_name: str,
        selection_name: str,
    ) -> None:
        """Update the exercise param selection."""
        source = getattr(self, source_name)
        selection = getattr(self, selection_name)

        # Populate selection.
        for item in items:
            source.append(data=item)

            # Set default.
            alias, _ = item
            if default == alias:
                selection.value = source.find(item)


class ParamsWidgets(HttpPutMixin, WidgetMixin, Params):
    """Exercise params widgets."""

    title = ''
    """The box-container title (`str`).
    """

    def __init__(self) -> None:
        """Construct a widgets."""
        super().__init__()

        # Styles.
        self.style_label = Pack(padding=(7, 0, 7, 20))

        # Title.
        self.label_title = TitleLabel(text=self.title)

        # fmt: off
        # Selection labels.
        self.label_start = Label('Начало периода:', style=self.style_label)
        self.label_end = Label('Конец периода:', style=self.style_label)
        self.label_category = Label('Категория:', style=self.style_label)
        self.label_progres = Label('Стадия изучения:', style=self.style_label)

        # Selections.
        self.selection_start_date = Selection(accessor='name', items=self.source_start_date)  # noqa: E501
        self.selection_end_date = Selection(accessor='name', items=self.source_end_date)  # noqa: E501
        self.selection_category = Selection(accessor='name', items=self.source_category)  # noqa: E501
        self.selection_progress = Selection(accessor='name', items=self.source_progress)  # noqa: E501
        self.input_count_first = NumberInput(step=10, min=0)
        self.input_count_last = NumberInput(step=10, min=0)

        # Switches for enable/untenable params.
        self.switch_count_first = Switch('Первые', on_change=self.first_switch_handler)  # noqa: E501
        self.switch_count_first.style = self.style_label
        self.switch_count_last = Switch('Последние', on_change=self.last_switch_handler)  # noqa: E501
        self.switch_count_last.style = self.style_label

        # Buttons.
        self.btn_save_params = BtnApp('Сохранить настройки', on_press=self.save_params_handler)  # noqa: E501
        self.btn_goto_exercise = BtnApp('Начать упражнение', on_press=self.goto_box_exercise_handler)  # noqa: E501
        # fmt: on

    async def goto_box_exercise_handler(self, widget: toga.Widget) -> None:
        """Go to exercise page box, button handler."""
        raise NotImplementedError(
            'Subclasses must provide a goto_exercise_box_handler() method.'
        )

    async def save_params_handler(self, _: toga.Widget) -> None:
        """Request to save exercise params, button handler."""
        raise NotImplementedError(
            'Subclasses must provide a save_params_handler() method.'
        )

    def first_switch_handler(self, widget: toga.Widget) -> None:
        """Count of first added words, switch handler."""
        if self.switch_count_first.value:
            self.switch_count_last.value = False

    def last_switch_handler(self, widget: toga.Widget) -> None:
        """Count of last added words, switch handler."""
        if self.switch_count_last.value:
            self.switch_count_first.value = False


class ParamsLayout(ParamsWidgets, BaseBox):
    """Exercise params layout."""

    def __init__(self) -> None:
        """Construct the layout."""
        super().__init__()

        # Styles.
        self.style_box_selection = Pack(padding=(2, 0, 2, 0))

        # Exercise parameter widgets are enclosed in boxes.
        self.construct_selection_boxes()

        # Exercise parameter boxes are enclosed in ``box_params``.
        self.box_params = toga.Box(style=Pack(direction=COLUMN, flex=1))

        # DOM.
        self.add(
            self.label_title,
            self.box_params,
            self.btn_goto_exercise,
            self.btn_save_params,
        )
        self.box_params.add(
            self.box_selection_start,
            self.box_selection_end,
            self.box_selection_category,
            self.box_selection_progress,
            self.box_input_first,
            self.box_input_last,
        )

    def construct_selection_boxes(self) -> None:
        """Construct a selection boxes."""
        self.box_selection_start = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(children=[self.label_start]),
                FlexBox(children=[self.selection_start_date]),
            ],
        )
        self.box_selection_start.style.padding_top = 4
        self.box_selection_end = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(children=[self.label_end]),
                FlexBox(children=[self.selection_end_date]),
            ],
        )
        self.box_selection_category = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(children=[self.label_category]),
                FlexBox(children=[self.selection_category]),
            ],
        )
        self.box_selection_progress = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(children=[self.label_progres]),
                FlexBox(children=[self.selection_progress]),
            ],
        )
        self.box_input_first = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(
                    children=[self.switch_count_first],
                    style=Pack(direction=COLUMN, padding_right=20),
                ),
                FlexBox(
                    children=[self.input_count_first],
                    style=Pack(direction=COLUMN),
                ),
            ],
        )
        self.box_input_last = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(
                    children=[self.switch_count_last],
                    style=Pack(direction=COLUMN, padding_right=20),
                ),
                FlexBox(
                    children=[self.input_count_last],
                    style=Pack(direction=COLUMN),
                ),
            ],
        )
