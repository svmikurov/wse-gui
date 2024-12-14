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
            self.populate_selections()

    def request_params(self) -> None:
        """Request a exercise params."""
        response = request_get(self.url)
        if response.status_code == HTTPStatus.OK:
            self.params = response.json()

    def populate_selections(self) -> None:
        """Populate selections."""
        categories = self.params['exercise_choices']['categories']
        self.source_category.update_data(categories)

    ####################################################################
    # Button handlers

    def set_saved_params(self) -> None:
        """Populate widgets by saved params, bnt handler."""
        pass

    def set_default_params(self) -> None:
        """Populate widgets by default params, bnt handler."""
        pass

    def save_params(self) -> None:
        """Save params, bnt handler."""
        pass

    # End Button handler
    ####################

    def print_selection(self, _: toga.Selection) -> None:
        """Print selection."""
        print(f'============ {self.source_category.value = }')


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
        self.btn_print_value = BtnApp('Напечатай выбор', on_press=self.print_selection)  # noqa: E501
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
            self.btn_print_value,
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
