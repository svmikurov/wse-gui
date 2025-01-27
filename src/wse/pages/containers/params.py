"""Exercise params."""

from typing import Callable

import toga
from toga import colors, Selection
from toga.constants import COLUMN
from toga.style import Pack

from wse.controllers.params import ControllerParams
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol, BoxFlexRow
from wse.pages.widgets.box_page import BaseBox, WidgetMixin
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import LabelParam, TitleLabel
from wse.pages.widgets.number_input import NumberInputApp
from wse.pages.widgets.switch import SwitchApp


class ParamsWidgets(WidgetMixin):
    """Exercise params widgets."""

    title = ''
    url: str
    goto_exercise_handler: Callable
    goto_table_handler: Callable

    def __init__(self, controller: ControllerParams) -> None:
        """Construct a widgets."""
        super().__init__()
        self._plc = controller
        self._plc.url = self.url

        # Title
        self._label_title = TitleLabel(text=self.title)

        # fmt: off
        # Selections
        self._selection_category = Selection(accessor='name', items=self._plc.category)  # noqa: E501
        self._selection_source = Selection(accessor='name', items=self._plc.source)  # noqa: E501
        self._selection_order = Selection(accessor='name', items=self._plc.order)  # noqa: E501
        self._selection_period_start_date = Selection(accessor='name', items=self._plc.period_start_date)  # noqa: E501
        self._selection_period_end_date = Selection(accessor='name', items=self._plc.period_end_date)  # noqa: E501

        # Switches of count
        self._switch_is_first = SwitchApp(text='', on_change=self._plc.is_first.update_value)  # noqa: E501
        self._switch_is_last = SwitchApp(text='', on_change=self._plc.is_last.update_value)  # noqa: E501

        # NumberInputs
        self._input_count_first = NumberInputApp(step=10, min=0, on_change=self._plc.count_first.update_value)  # noqa: E501
        self._input_count_last = NumberInputApp(step=10, min=0, on_change=self._plc.count_last.update_value)  # noqa: E501

        # Switches of progress
        self._switch_study = SwitchApp(text='', on_change=self._plc.progress.study.update_value)  # noqa: E501
        self._switch_repeat = SwitchApp(text='', on_change=self._plc.progress.repeat.update_value)  # noqa: E501
        self._switch_examination = SwitchApp(text='', on_change=self._plc.progress.examination.update_value)  # noqa: E501
        self._switch_know = SwitchApp(text='', on_change=self._plc.progress.know.update_value)  # noqa: E501

        # Switch of favorites
        self.switch_favorites = SwitchApp(text='', on_change=self._plc.favorites.update_value)  # noqa: E501

        # Timeout
        self._switch_timeout = SwitchApp(text='', on_change=self._plc.has_timeout.update_value)  # noqa: E501
        self._input_timeout = NumberInputApp(step=1, min=1, on_change=self._plc.timeout.update_value)  # noqa: E501

        # Buttons
        self._btn_reset_params = BtnApp('Сбросить выбор', on_press=self._display_confirm_reset_handler)  # noqa: E501
        self._btn_save_params = BtnApp('Сохранить выбор', on_press=self._display_confirm_save_handler)  # noqa: E501
        self._btn_goto_table = BtnApp('Список выбранных', on_press=self._display_selected_handler)  # noqa: E501
        self._btn_set_saved_params = BtnApp('Сохраненный выбор', on_press=self._set_saved_params_handler)  # noqa: E501
        self._btn_goto_exercise = BtnApp('Начать упражнение', on_press=self._start_exercise_handler)  # noqa: E501
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Confirm buttons
        self._btn_cancel_save = BtnApp('Отмена', on_press=self._undisplay_confirm_save_handler)  # noqa: E501
        self._btn_cancel_save.style.background_color=colors.TOMATO
        self._btn_confirm_save = BtnApp('Сохранить', on_press=self._confirm_save_handler)  # noqa: E501
        self._btn_confirm_save.style.background_color=colors.GREEN
        self._btn_cancel_reset = BtnApp('Отмена', on_press=self._undisplay_confirm_reset_handler)  # noqa: E501
        self._btn_cancel_reset.style.background_color=colors.TOMATO
        self._btn_confirm_reset = BtnApp('Сбросить', on_press=self._confirm_reset_handler)  # noqa: E501
        self._btn_confirm_reset.style.background_color=colors.GREEN
        # Divider
        self._box_divider = toga.Box(
            children=[toga.Divider()],
            style=Pack(direction=COLUMN, padding=(5, 10, 5, 10), background_color=colors.WHITE)  # noqa: E501
        )
        # fmt: on

        # Listeners
        self._plc.is_first.add_listener(self._switch_is_first)
        self._plc.is_last.add_listener(self._switch_is_last)
        self._plc.count_first.add_listener(self._input_count_first)
        self._plc.count_last.add_listener(self._input_count_last)
        self._plc.progress.study.add_listener(self._switch_study)
        self._plc.progress.repeat.add_listener(self._switch_repeat)
        self._plc.progress.examination.add_listener(self._switch_examination)
        self._plc.progress.know.add_listener(self._switch_know)
        self._plc.favorites.add_listener(self.switch_favorites)
        self._plc.has_timeout.add_listener(self._switch_timeout)
        self._plc.timeout.add_listener(self._input_timeout)

    async def on_open(self, widget: toga.Widget) -> None:
        """Request exercise params and populate selections."""
        await self._plc.on_open(widget)

    ####################################################################
    # Button handlers

    @classmethod
    async def _start_exercise_handler(cls, widget: toga.Widget) -> None:
        await cls.goto_exercise_handler(widget)

    def _set_saved_params_handler(self, _: toga.Widget) -> None:
        self._plc.set_saved_params()

    async def _reset_params_handler(self, _: toga.Widget) -> None:
        """Populate widgets by default params, button handler."""
        await self._plc.update_params()

    async def _save_params_handler(self, _: toga.Widget) -> None:
        await self._plc.request_save_lookup_conditions()
        await self._plc.update_params()
        self._plc.set_saved_params()

    @classmethod
    async def _display_selected_handler(cls, widget: toga.Widget) -> None:
        await cls.goto_table_handler(widget)

    #########
    # Confirm

    def _display_confirm_save_handler(self, _: toga.Widget) -> None:
        raise NotImplementedError()

    def _confirm_save_handler(self, widget: toga.Widget) -> None:
        raise NotImplementedError()

    def _undisplay_confirm_save_handler(self, _: toga.Widget) -> None:
        """Replace confirm to save button, button handler."""
        raise NotImplementedError()

    def _display_confirm_reset_handler(self, _: toga.Widget) -> None:
        raise NotImplementedError()

    async def _confirm_reset_handler(self, widget: toga.Widget) -> None:
        raise NotImplementedError()

    def _undisplay_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Replace confirm to reset button, button handler."""
        raise NotImplementedError()


class ParamsLayout(ParamsWidgets, BaseBox):
    """Exercise params layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the layout."""
        super().__init__(*args, **kwargs)

        # Styles
        self._style_box_selection = Pack(padding=(2, 0, 2, 0))

        # Exercise params widgets are enclosed in boxes.
        self._include_selections_to_boxes()
        self._include_number_inputs_to_boxes()
        self._include_progress_switches_to_boxes()
        self._include_favorites_switch_to_box()
        self._include_timeout_to_box()

        # When saving settings, the save button
        # is replaced by a confirm button.
        self._create_box_confirm_save()
        self._create_box_confirm_reset()
        self._create_box_save_reset()

        # Exercise parameter boxes are enclosed in ``box_params``.
        self._box_params = BoxFlexCol()

        # Box Params is included in scroll container.
        self._scroll_container = toga.ScrollContainer(
            style=Pack(flex=1),
            content=self._box_params,
        )

        # DOM
        self.add(
            self._label_title,
            self._scroll_container,
            self._box_divider,
            self._btn_goto_table,
            self._box_save_reset,
            self._btn_set_saved_params,
            self._btn_goto_exercise,
            self._btn_goto_back,
        )
        self._box_params.add(
            # Selections
            self._box_selection_category,
            self._box_selection_source,
            self._box_selection_order,
            self._box_selection_period_start_date,
            self._box_selection_period_end_date,
            # NumberInputs
            self._box_nuber_input_first,
            self._box_nuber_input_last,
            self._box_timeout,
            # Progress switchers
            self._box_progress_switchers_line1,
            self._box_progress_switchers_line2,
            # Favorites
            self._box_favorites,
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Request exercise params and populate selections."""
        await super().on_open(widget)
        self._select_widgets_to_display()

    #####################################################################
    # Create boxes

    def _include_selections_to_boxes(self) -> None:
        self._box_selection_category = toga.Box(
            style=self._style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Категория:')]),
                BoxFlexCol(children=[self._selection_category]),
            ],
        )
        self._box_selection_source = toga.Box(
            style=self._style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Источник:')]),
                BoxFlexCol(children=[self._selection_source]),
            ],
        )
        self._box_selection_order = toga.Box(
            style=self._style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Порядок перевода:')]),
                BoxFlexCol(children=[self._selection_order]),
            ],
        )
        self._box_selection_period_start_date = toga.Box(
            style=self._style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Начало периода:')]),
                BoxFlexCol(children=[self._selection_period_start_date]),
            ],
        )
        self._box_selection_period_end_date = toga.Box(
            style=self._style_box_selection,
            children=[
                BoxFlexCol(children=[LabelParam('Конец периода:')]),
                BoxFlexCol(children=[self._selection_period_end_date]),
            ],
        )

    def _include_number_inputs_to_boxes(self) -> None:
        self._box_nuber_input_first = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Первые:')]),
                        BoxFlexRow(children=[self._switch_is_first]),
                    ],
                ),
                BoxFlexCol(children=[self._input_count_first]),
            ]
        )
        self._box_nuber_input_last = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Последние:')]),
                        BoxFlexRow(children=[self._switch_is_last]),
                    ],
                ),
                BoxFlexCol(children=[self._input_count_last]),
            ]
        )

    def _include_progress_switches_to_boxes(self) -> None:
        self._box_progress_switchers_line1 = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Изучаю')]),
                        BoxFlexRow(children=[self._switch_study]),
                    ]
                ),
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Повторяю')]),
                        BoxFlexRow(children=[self._switch_repeat]),
                    ]
                ),
            ]
        )
        self._box_progress_switchers_line2 = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Проверяю')]),
                        BoxFlexRow(children=[self._switch_examination]),
                    ]
                ),
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Знаю')]),
                        BoxFlexRow(children=[self._switch_know]),
                    ]
                ),
            ]
        )

    def _include_favorites_switch_to_box(self) -> None:
        self._box_favorites = toga.Box(
            children=[
                BoxFlexRow(children=[LabelParam('Только избранное')]),
                BoxFlexRow(children=[self.switch_favorites]),
            ]
        )

    def _include_timeout_to_box(self) -> None:
        self._box_timeout = toga.Box(
            children=[
                BoxFlexRow(
                    children=[
                        BoxFlexRow(children=[LabelParam('Таймаут:')]),
                        BoxFlexRow(children=[self._switch_timeout]),
                    ],
                ),
                BoxFlexCol(children=[self._input_timeout]),
            ]
        )

    def _create_box_confirm_save(self) -> None:
        self._box_confirm_save = toga.Box(
            children=[self._btn_cancel_save, self._btn_confirm_save]
        )

    def _create_box_confirm_reset(self) -> None:
        self._box_confirm_reset = toga.Box(
            children=[self._btn_cancel_reset, self._btn_confirm_reset]
        )

    def _create_box_save_reset(self) -> None:
        """Save or reset params the container of buttons."""
        self._box_save_reset = toga.Box(
            children=[self._btn_save_params, self._btn_reset_params]
        )

    #####################################################################
    # Button handlers

    ##############
    # Save confirm

    def _display_confirm_save_handler(self, _: toga.Widget) -> None:
        """Display confirm, button handler."""
        self.replace(self._box_save_reset, self._box_confirm_save)

    async def _confirm_save_handler(self, widget: toga.Widget) -> None:
        """Confirm save params, button handler."""
        await self._save_params_handler(widget)
        self._undisplay_confirm_save_handler(widget)

    def _undisplay_confirm_save_handler(self, _: toga.Widget) -> None:
        """Replace confirm to save button, button handler."""
        self.replace(self._box_confirm_save, self._box_save_reset)

    ###############
    # Reset confirm

    def _display_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Display confirm, button handler."""
        self.replace(self._box_save_reset, self._box_confirm_reset)

    async def _confirm_reset_handler(self, widget: toga.Widget) -> None:
        """Confirm reset params, button handler."""
        await self._reset_params_handler(widget)
        self._undisplay_confirm_reset_handler(widget)

    def _undisplay_confirm_reset_handler(self, _: toga.Widget) -> None:
        """Replace confirm to reset button, button handler."""
        self.replace(self._box_confirm_reset, self._box_save_reset)

    #####################################################################
    # Select widgets to display

    def _select_widgets_to_display(self) -> None:
        if 'order' in self._plc.lookup_conditions:
            self._insert_order_param()
        else:
            self._remove_order_param()

    def _insert_order_param(self) -> None:
        order_param_index = 2
        self._box_params.insert(order_param_index, self._box_selection_order)

    def _remove_order_param(self) -> None:
        self._box_params.remove(self._box_selection_order)
