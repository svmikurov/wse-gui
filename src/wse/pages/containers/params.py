"""Exercise params."""

import toga
from toga import Selection
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_foreign_exercise_handler,
)
from wse.pages.widgets.box import BoxFlexCol, BoxFlexRow
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import LabelParam, TitleLabel
from wse.pages.widgets.number_input import NumberInputApp
from wse.pages.widgets.switch import SwitchApp


class ParamsWidgets(HttpPutMixin, WidgetMixin):
    """Exercise params widgets."""

    title = ''
    """The exercise page title (`str`).
    """

    # TODO: Fix controller annotation.
    def __init__(self, controller: object) -> None:
        """Construct a widgets."""
        super().__init__()

        # Widgets use public attributes of the controller.
        for attr_name in dir(controller):
            if not attr_name.startswith('_'):
                attr = getattr(controller, attr_name)
                setattr(self, attr_name, attr)

        # TODO: Add annotations for controller attrs.

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
        self.switch_study = SwitchApp(text='', on_change=self.progress.study.update_value)  # noqa: E501
        self.switch_repeat = SwitchApp(text='', on_change=self.progress.repeat.update_value)  # noqa: E501
        self.switch_examination = SwitchApp(text='', on_change=self.progress.examination.update_value)  # noqa: E501
        self.switch_know = SwitchApp(text='', on_change=self.progress.know.update_value)  # noqa: E501
        # Switches are listeners.
        self.progress.study.add_listener(self.switch_study)
        self.progress.repeat.add_listener(self.switch_repeat)
        self.progress.examination.add_listener(self.switch_examination)
        self.progress.know.add_listener(self.switch_know)

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

    async def start_exercise_handler(self, widget: toga.Widget) -> None:
        """Start exercise, button handler."""
        await goto_foreign_exercise_handler(widget)

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

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the layout."""
        super().__init__(*args, **kwargs)

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
