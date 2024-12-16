"""Exercise params."""

from http import HTTPStatus

import toga
from toga import Label, Selection
from toga.constants import COLUMN
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin, request_get, \
    request_put_async
from wse.handlers.goto_handler import goto_back_handler
from wse.source.params import ItemSource
from wse.widgets.box import FlexBox
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel

ACCESSORS = ['alias', 'name']


class Params:
    """Exercise params."""

    url = ''
    """Url to get exercise params with GET method and to save
    user lookup conditions with PUT method (`str`).
    """

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self.exercise_choices: dict | None = None
        self.lookup_conditions: dict | None = None
        self.source_category = ItemSource(ACCESSORS)

    ####################################################################
    # Logic

    async def on_open(self, _: toga.Widget) -> None:
        """Request params and populate selections."""
        if not self.exercise_choices:
            self.request_params()
            self.populate_selections_default()

    def populate_selections_default(self) -> None:
        """Populate selections."""
        categories = self.exercise_choices['categories']
        self.source_category.clear()
        self.source_category.update_data(categories)
        self.source_category.set_value(None)

    def set_saved_params(self) -> None:
        """Set saved choices."""
        category = self.lookup_conditions['category']
        self.source_category.set_value(category)

    ####################################################################
    # HTTP requests

    def request_params(self) -> None:
        """Request a exercise params."""
        response = request_get(self.url)
        if response.status_code == HTTPStatus.OK:
            params = response.json()
            self.lookup_conditions = params['lookup_conditions']
            self.exercise_choices = params['exercise_choices']

    async def request_save_lookup_conditions(self):
        """Request to save user lookup conditions."""
        lookup_conditions = {
            'category': self.source_category.value.alias,
        }
        await request_put_async(url=self.url, payload=lookup_conditions)


class ParamsWidgets(HttpPutMixin, WidgetMixin, Params):
    """Exercise params widgets."""

    title = ''
    """The page title (`str`).
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
        self.label_category = Label('Категория:', style=self.style_label)

        # Selections.
        self.selection_category = Selection(accessor='name', items=self.source_category)  # noqa: E501

        # Buttons.
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

    def reset_params_handler(self, _: toga.Widget) -> None:
        """Populate widgets by default params, button handler."""
        self.request_params()
        self.populate_selections_default()

    async def save_params_handler(self, _: toga.Widget) -> None:
        """Save selected params, button handler."""
        await self.request_save_lookup_conditions()


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

        # Exercise params buttons are enclosed in ``box_params_btns``.
        self.box_params_btns = toga.Box(style=Pack(direction=COLUMN, flex=1))

        # DOM.
        self.add(
            self.label_title,
            self.box_params,
            self.box_params_btns,
        )
        self.box_params.add(
            self.box_selection_category,
        )
        self.box_params_btns.add(
            self.btn_goto_exercise,
            self.btn_set_saved_params,
            self.btn_reset_params,
            self.btn_save_params,
            self.btn_goto_back,
        )

    def construct_selection_boxes(self) -> None:
        """Construct a selection boxes."""
        self.box_selection_category = toga.Box(
            style=self.style_box_selection,
            children=[
                FlexBox(children=[self.label_category]),
                FlexBox(children=[self.selection_category]),
            ],
        )
