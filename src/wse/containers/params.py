"""Exercise params."""

from http import HTTPStatus

import toga
from toga import Label, NumberInput, Selection, Switch
from toga.constants import COLUMN
from toga.sources import Listener, Row
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin, request_get
from wse.source.params import ItemSource, DefaultSource
from wse.widgets.box import FlexBox
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel


class Params:
    """Exercise params."""

    url = ''
    """The exercise params url (`str`).
    """

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self.source_category = ItemSource(['alias', 'name'])

    async def on_open(self, _: toga.Widget) -> None:
        """Request params and update widgets when box open."""
        params = self.request_params()
        if params:
            self.update_params_source(params)

    def request_params(self) -> dict | None:
        """Request a exercise params."""
        response = request_get(self.url)
        if response.status_code == HTTPStatus.OK:
            return response.json()

    def update_params_source(self, params: dict) -> None:
        """Update selection source."""
        categories = params['exercise_choices']['categories']
        self.source_category.update_items(categories)


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
        self.selection_category = Selection(accessor='name', items=self.source_category)

        # Buttons.
        self.btn_save_params = BtnApp('Сохранить настройки', on_press=self.save_params_handler)  # noqa: E501
        self.btn_goto_exercise = BtnApp('Начать упражнение', on_press=self.goto_box_exercise_handler)  # noqa: E501
        # fmt: on

    async def goto_box_exercise_handler(self, widget: toga.Widget) -> None:
        """Go to exercise page box, button handler."""
        raise NotImplementedError(
            'Subclasses must provide a goto_exercise_box_handler() method.'
        )

    async def save_params_handler(self, widget: toga.Widget) -> None:
        """Request to save exercise params, button handler."""
        raise NotImplementedError(
            'Subclasses must provide a save_params_handler() method.'
        )


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
            self.box_selection_category,
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
