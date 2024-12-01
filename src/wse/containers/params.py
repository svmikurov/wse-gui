"""Exercise params."""

from http import HTTPStatus

import toga
from toga import Label, NumberInput, Switch, Selection
from toga.constants import COLUMN
from toga.sources import ListSource
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin, request_get
from wse.widgets.box import FlexBox
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel
from wse.widgets.selection import BaseSelection


class Params:
    """Exercise params."""

    url = ''
    """The exercise params url (`str`).
    """

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self.accessors_category = ['alias', 'name']

        # Sources.
        self.source = ListSource(accessors=self.accessors_category)

    async def on_open(self, _: toga.Widget) -> None:
        """Request and fill params data of box when box open."""
        self.request_params()

    def request_params(self) -> None:
        """Request exercise params."""
        response = request_get(url=self.url)

        if response.status_code == HTTPStatus.OK:
            params = response.json()

    # def get_params(self) -> dict[str, str | list | None]:
    #     """Extract exercise params from widgets."""
    #     # NumberInput return Decimal objects or None.
    #     count_first = int(self.input_count_first.value or 0)
    #     count_last = int(self.input_count_last.value or 0)
    #     params = {
    #         'period_start_date': self.selection_start_period.get_alias(),
    #         'period_end_date': self.selection_end_period.get_alias(),
    #         'category': self.selection_category.get_alias(),
    #         'progress': [self.selection_progress.get_alias()],
    #         'count_first': count_first * self.switch_count_first.value,
    #         'count_last': count_last * self.switch_count_last.value,
    #     }
    #     return params
    #
    # def set_params(self, value: dict) -> None:
    #     """Set exercise params to widgets."""
    #     # Initial values for the selection.
    #     defaults = value['lookup_conditions']
    #     # Items to display for selection.
    #     items = value['exercise_choices']
    #
    #     self.selection_start_period.set_items(
    #         items['edge_period_items'], defaults['period_start_date']
    #     )
    #     self.selection_end_period.set_items(
    #         items['edge_period_items'], defaults['period_end_date']
    #     )
    #     self.selection_category.set_items(
    #         items['categories'], defaults['category']
    #     )
    #     self.selection_progress.set_items(
    #         items['progress'], defaults['progress']
    #     )  # fmt: skip
    #     if bool(defaults['count_first']):
    #         self.input_count_first.value = defaults['count_first']
    #         self.switch_count_first.value = True
    #         self.switch_count_last.value = False
    #     if bool(defaults['count_last']):
    #         self.input_count_last.value = defaults['count_last']
    #         self.switch_count_last.value = True
    #         self.switch_count_first.value = False

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

        # Switches for enable/untenable params.
        self.switch_count_first = Switch('Первые', on_change=self.first_switch_handler)  # noqa: E501
        self.switch_count_first.style = self.style_label
        self.switch_count_last = Switch('Последние', on_change=self.last_switch_handler)  # noqa: E501
        self.switch_count_last.style = self.style_label

        # Selections.
        self.selection_start_period = BaseSelection()
        self.selection_end_period = BaseSelection()
        self.selection_category = Selection(accessor='name', items=self.source)
        self.selection_progress = BaseSelection()
        self.input_count_first = NumberInput(step=10, min=0)
        self.input_count_last = NumberInput(step=10, min=0)

        # General buttons.
        self.btn_save_params = BtnApp('Сохранить настройки', on_press=self.save_params_handler)  # noqa: E501
        self.btn_goto_exercise = BtnApp('Начать упражнение', on_press=self.goto_box_exercise_handler)  # noqa: E501
        # fmt: on

    async def on_open(self, widget: toga.Widget) -> None:
        """Request and fill params data of box when box open."""
        await super().on_open(widget)

    ####################################################################
    # Button callback functions

    async def goto_box_exercise_handler(self, widget: toga.Widget) -> None:
        """Go to foreign exercise page box, button handler."""
        raise NotImplementedError(
            'Subclasses must provide a goto_exercise_box_handler() method.'
        )

    async def save_params_handler(self, _: toga.Widget) -> None:
        """Request to save foreign exercise params, button handler."""
        raise NotImplementedError(
            'Subclasses must provide a goto_exercise_box_handler() method.'
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
                FlexBox(children=[self.selection_start_period]),
            ],
        )
        self.box_selection_start.style.padding_top = 4
        self.box_selection_end = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(children=[self.label_end]),
                FlexBox(children=[self.selection_end_period]),
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
