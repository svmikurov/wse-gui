"""Exercise params."""

import toga
from toga import Selection, colors
from toga.constants import COLUMN
from toga.style import Pack

from wse.contrib.http_requests import HttpPutMixin
from wse.controllers.params import ControllerParams
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
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

    def __init__(self, controller: ControllerParams) -> None:
        """Construct a widgets."""
        super().__init__()
        self.plc = controller
        # To override
        self.goto_exercise_handler = None
        self.goto_selected_handler = None

        # Title
        self.label_title = TitleLabel(text=self.title)

        # fmt: off
        # Selections
        self.selection_category = Selection(accessor='name', items=self.plc.category)  # noqa: E501
        self.selection_source = Selection(accessor='name', items=self.plc.source)  # noqa: E501
        self.selection_order = Selection(accessor='name', items=self.plc.order)  # noqa: E501
        self.selection_period_start_date = Selection(accessor='name', items=self.plc.period_start_date)  # noqa: E501
        self.selection_period_end_date = Selection(accessor='name', items=self.plc.period_end_date)  # noqa: E501

        # Switches of count
        self.switch_is_first = SwitchApp(text='', on_change=self.plc.is_first.update_value)  # noqa: E501
        self.switch_is_last = SwitchApp(text='', on_change=self.plc.is_last.update_value)  # noqa: E501

        # NumberInputs
        self.input_count_first = NumberInputApp(step=10, min=0, on_change=self.plc.count_first.update_value)  # noqa: E501
        self.input_count_last = NumberInputApp(step=10, min=0, on_change=self.plc.count_last.update_value)  # noqa: E501

        # Switches of progress
        self.switch_study = SwitchApp(text='', on_change=self.plc.progress.study.update_value)  # noqa: E501
        self.switch_repeat = SwitchApp(text='', on_change=self.plc.progress.repeat.update_value)  # noqa: E501
        self.switch_examination = SwitchApp(text='', on_change=self.plc.progress.examination.update_value)  # noqa: E501
        self.switch_know = SwitchApp(text='', on_change=self.plc.progress.know.update_value)  # noqa: E501

        # Switch of favorites
        self.switch_favorites = SwitchApp(text='', on_change=self.plc.favorites.update_value)  # noqa: E501

        # Timeout
        self.switch_timeout = SwitchApp(text='', on_change=self.plc.has_timeout.update_value)  # noqa: E501
        self.input_timeout = NumberInputApp(step=1, min=1, on_change=self.plc.timeout.update_value)  # noqa: E501

        # Buttons
        self.btn_reset_params = BtnApp('Сбросить выбор', on_press=self.display_confirm_reset_handler)  # noqa: E501
        self.btn_save_params = BtnApp('Сохранить выбор', on_press=self.display_confirm_save_handler)  # noqa: E501
        self.btn_goto_selected = BtnApp('Список выбранных', on_press=self.display_selected_handler)  # noqa: E501
        self.btn_set_saved_params = BtnApp('Сохраненный выбор', on_press=self.set_saved_params_handler)  # noqa: E501
        self.btn_goto_exercise = BtnApp('Начать упражнение', on_press=self.start_exercise_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)  # noqa: E501

        # Confirm buttons
        self.btn_cancel_save = BtnApp('Назад', on_press=self.undisplay_confirm_save_handler)  # noqa: E501
        self.btn_confirm_save = BtnApp('Сохранить', on_press=self.confirm_save_handler)  # noqa: E501
        self.btn_cancel_reset = BtnApp('Назад', on_press=self.undisplay_confirm_reset_handler)  # noqa: E501
        self.btn_confirm_reset = BtnApp('Сбросить', on_press=self.confirm_reset_handler)  # noqa: E501
        # Divider
        self.box_divider = toga.Box(
            children=[toga.Divider()],
            style=Pack(direction=COLUMN, padding=(5, 10, 5, 10), background_color=colors.WHITE)  # noqa: E501
        )
        # fmt: on

        # Listeners
        self.plc.is_first.add_listener(self.switch_is_first)
        self.plc.is_last.add_listener(self.switch_is_last)
        self.plc.count_first.add_listener(self.input_count_first)
        self.plc.count_last.add_listener(self.input_count_last)
        self.plc.progress.study.add_listener(self.switch_study)
        self.plc.progress.repeat.add_listener(self.switch_repeat)
        self.plc.progress.examination.add_listener(self.switch_examination)
        self.plc.progress.know.add_listener(self.switch_know)
        self.plc.favorites.add_listener(self.switch_favorites)
        self.plc.has_timeout.add_listener(self.switch_timeout)
        self.plc.timeout.add_listener(self.input_timeout)

    async def on_open(self, widget: toga.Widget) -> None:
        """Request exercise params and populate selections."""
        await self.plc.on_open(widget)

    ####################################################################
    # Button handlers

    async def start_exercise_handler(self, widget: toga.Widget) -> None:
        """Start exercise, button handler."""
        await self.goto_exercise_handler(widget)

    def set_saved_params_handler(self, _: toga.Widget) -> None:
        """Set saved params choice, button handler."""
        self.plc.set_saved_params()

    async def reset_params_handler(self, _: toga.Widget) -> None:
        """Populate widgets by default params, button handler."""
        await self.plc.update_params()

    async def save_params_handler(self, _: toga.Widget) -> None:
        """Save selected params, button handler."""
        await self.plc.request_save_lookup_conditions()

    async def display_selected_handler(self, widget: toga.Widget) -> None:
        """Save selected params, button handler."""
        await self.goto_selected_handler(widget)

    #########
    # Confirm

    def display_confirm_save_handler(self, _: toga.Widget) -> None:
        """Display confirm, button handler."""
        raise NotImplementedError()

    def confirm_save_handler(self, widget: toga.Widget) -> None:
        """Confirm save params, button handler."""
        raise NotImplementedError()

    def undisplay_confirm_save_handler(self, _: toga.Widget) -> None:
        """Replace confirm to save button, button handler."""
        raise NotImplementedError()

    def display_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Display confirm, button handler."""
        raise NotImplementedError()

    async def confirm_reset_handler(self, widget: toga.Widget) -> None:
        """Confirm reset params, button handler."""
        raise NotImplementedError()

    def undisplay_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Replace confirm to reset button, button handler."""
        raise NotImplementedError()


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

        # When saving settings, the save button
        # is replaced by a confirm button.
        self.create_box_confirm_save()
        self.create_box_confirm_reset()
        self.create_box_save_reset()

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
            self.box_divider,
            self.box_save_reset,
            self.btn_set_saved_params,
            self.btn_goto_selected,
            self.btn_goto_exercise,
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

    async def on_open(self, widget: toga.Widget) -> None:
        """Request exercise params and populate selections."""
        await super().on_open(widget)
        self._select_widgets_to_display()

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

    def create_box_confirm_save(self) -> None:
        """Create save params confirm widget box."""
        self.box_confirm_save = toga.Box(
            children=[self.btn_cancel_save, self.btn_confirm_save]
        )

    def create_box_confirm_reset(self) -> None:
        """Create reset params confirm widget box."""
        self.box_confirm_reset = toga.Box(
            children=[self.btn_cancel_reset, self.btn_confirm_reset]
        )

    def create_box_save_reset(self) -> None:
        """Save or reset params the container of buttons."""
        self.box_save_reset = toga.Box(
            children=[self.btn_save_params, self.btn_reset_params]
        )

    #####################################################################
    # Button handlers

    ##############
    # Save confirm

    def display_confirm_save_handler(self, _: toga.Widget) -> None:
        """Display confirm, button handler."""
        self.replace(self.box_save_reset, self.box_confirm_save)

    async def confirm_save_handler(self, widget: toga.Widget) -> None:
        """Confirm save params, button handler."""
        await self.save_params_handler(widget)
        self.undisplay_confirm_save_handler(widget)

    def undisplay_confirm_save_handler(self, _: toga.Widget) -> None:
        """Replace confirm to save button, button handler."""
        self.replace(self.box_confirm_save, self.box_save_reset)

    ###############
    # Reset confirm

    def display_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Display confirm, button handler."""
        self.replace(self.box_save_reset, self.box_confirm_reset)

    async def confirm_reset_handler(self, widget: toga.Widget) -> None:
        """Confirm reset params, button handler."""
        await self.reset_params_handler(widget)
        self.undisplay_confirm_reset_handler(widget)

    def undisplay_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Replace confirm to reset button, button handler."""
        self.replace(self.box_confirm_reset, self.box_save_reset)

    #####################################################################
    # Select widgets to display

    def _select_widgets_to_display(self) -> None:
        if 'order' in self.plc.lookup_conditions:
            self._insert_order_param()
        else:
            self._remove_order_param()

    def _insert_order_param(self) -> None:
        order_param_index = 2
        self.box_params.insert(order_param_index, self.box_selection_order)

    def _remove_order_param(self) -> None:
        self.box_params.remove(self.box_selection_order)
