"""Exercise params."""

from http import HTTPStatus

import toga
from toga import Label, Selection
from toga.constants import COLUMN
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin, request_get
from wse.source.params import ItemSource
from wse.widgets.box import FlexBox
from wse.widgets.box_page import BaseBox, WidgetMixin
from wse.widgets.button import BtnApp
from wse.widgets.label import TitleLabel

ACCESSORS = ['alias', 'name']


class Params:
    """Exercise params."""

    url = ''
    """The exercise params url (`str`).
    """

    def __init__(self) -> None:
        """Construct the exercise params."""
        super().__init__()
        self.params = None

        # Source
        self.source_category = ItemSource(ACCESSORS)

    async def on_open(self, _: toga.Widget) -> None:
        """Request and populate selections."""
        if not self.params:
            self.request_params()
            self.populate_selections_default()

    def request_params(self) -> None:
        """Request a exercise params."""
        response = request_get(self.url)
        if response.status_code == HTTPStatus.OK:
            self.params = response.json()

    def populate_selections_default(self) -> None:
        """Populate selections."""
        categories = self.params['exercise_choices']['categories']
        self.source_category.update_data(categories)


    def


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
        self.selection_category = Selection(
            accessor='name',
            items=self.source_category,
        )

        # Buttons.
        self.btn_goto_exercise = BtnApp('Начать упражнение', on_press=self.goto_box_exercise_handler)  # noqa: E501
        self.btn_default_params = BtnApp('Выбор по-умолчанию', on_press=self.set_default_params_handler)  # noqa: E502
        self.btn_saved_params = BtnApp('Сохраненный выбор', on_press=self.set_saved_params_handler)  # noqa: E502
        self.btn_save_params = BtnApp('Сохранить выбор', on_press=self.save_params_handler)  # noqa: E501
        # fmt: on

    ####################################################################
    # Button handlers

    def start_exercise_handler(self, _: toga.Widget) -> None:
        """Start exercise, button handler"""
        pass

    def set_saved_params_handler(self, _: toga.Widget) -> None:
        """Set saved params choice, button handler."""
        pass

    def refresh_params_handler(self, _: toga.Widget) -> None:
        """Populate widgets by default params, button handler."""
        self.populate_selections_default()

    def save_params_handler(self, _: toga.Widget) -> None:
        """Save selected params, button handler."""
        pass


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

        # Exercise parameter buttons are enclosed in ``box_params_btns``.
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
            self.btn_default_params,
            self.btn_saved_params,
            self.btn_save_params,
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
