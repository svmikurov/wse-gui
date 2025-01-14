"""The page to explore Toga widgets."""

import toga
from toga import colors
from toga.constants import CENTER, COLUMN
from toga.style import Pack
from travertino.colors import NAMED_COLOR

from wse.contrib.timer import Timer
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexCol
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.progress_bar import ProgressBarApp


class Explorer(toga.Box):
    """The page to explore Toga widgets."""

    def __init__(self) -> None:
        """Construct the widgets."""
        super().__init__()
        self.time = Timer()

        # fmt: off
        self.title = toga.Label(text='Страница изучения виджетов.', style=Pack(text_align=CENTER))  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Progress bar
        self.time.timeout = 5
        self.progress_bar = ProgressBarApp(max=self.time.timeout)
        self.btn_start_progress_bar = BtnApp('Запустить прогресс', on_press=self._start_progress_bar)  # noqa: E501
        self.time.progress_bar_source.add_listener(self.progress_bar)

        # Divider
        self.box_divider = toga.Box(
            children=[toga.Divider()],
            style=Pack(
                direction=COLUMN,
                padding=(5, 10, 5, 10),
                background_color=colors.GREEN
            )
        )
        # fmt: on

        # Colors
        self._create_color_scroll()

    async def _start_progress_bar(self, _: toga.Widget) -> None:
        await self.time.start_counter()


class ExplorerLayout(Explorer):
    """Layout of explorer page."""

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        self.style.direction = COLUMN

        # Create widgets
        self._create_title_box()
        self._create_progress_bar_box()

        # DOM
        self.add(
            self.box_title,
            self.box_divider,
            self.box_progress_bar,
            self.color_scroll,
            self.btn_start_progress_bar,
            self.btn_goto_back,
        )

    def _create_title_box(self) -> None:
        self.box_title = toga.Box(
            style=Pack(
                background_color=colors.GREEN,
                direction=COLUMN,
            ),
            children=[self.title],
        )

    def _create_progress_bar_box(self) -> None:
        self.box_progress_bar = BoxFlexCol(children=[self.progress_bar])

    def _create_color_scroll(self) -> None:
        box_scroll = toga.Box(style=Pack(direction=COLUMN, flex=1))
        for color in NAMED_COLOR:
            box_scroll.add(
                toga.Button(style=Pack(background_color=color), text=color)
            )
        self.color_scroll = toga.ScrollContainer(
            style=Pack(flex=1),
            content=box_scroll,
        )
