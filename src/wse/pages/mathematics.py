"""Mathematics pages."""

import toga
from toga.constants import LEFT, RIGHT
from toga.style import Pack

from wse.pages.base import BasePage
from wse.pages.containers import FractionLayout, NumKeyboard
from wse.pages.widgets import (
    BoxFlexCol,
    BoxFlexRow,
    BtnApp,
    BtnBack,
)

NUM_FONT_SIZE = 48
HEIGHT_VS_FONT_SIZE_RATIO = 1.6
MAX_DIGIT_COUNT = 3
NUM_HEIGHT = int(NUM_FONT_SIZE * HEIGHT_VS_FONT_SIZE_RATIO)


class Panel(toga.Label):
    """One line panel widget."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        kwargs['text'] = kwargs.setdefault('text', '')
        super().__init__(*args, **kwargs)
        self.style.height = NUM_HEIGHT
        self.style.font_size = NUM_FONT_SIZE


class MathematicsMainPage(BasePage):
    """Mathematics exercises main pages."""

    title = 'Упражнения по математике'

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Navigation buttons
        _btn_goto_calculations = BtnApp(**self._nav.calculations)
        _btn_goto_fraction = BtnApp(**self._nav.fractions)

        # DOM
        self.add(
            BoxFlexRow(),
            _btn_goto_calculations,
            _btn_goto_fraction,
            BtnBack(),
        )


class CalculationsPage(BasePage):
    """Mathematics calculations page."""

    _padding = (30, 0, 0, 0)

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()

        # Panels
        self.question_text = Panel(style=Pack(flex=2, text_align=RIGHT))
        self.input_answer = Panel(style=Pack(flex=1, text_align=LEFT))
        self.panel_result = Panel(style=Pack(padding=self._padding))

        # Buttons
        self.num_keyboard = NumKeyboard(max_digit_count=MAX_DIGIT_COUNT)
        self.btn_submit = BtnApp('Ответить')

        # Inner boxes
        _box_task_inner = toga.Box(
            style=Pack(padding=self._padding),
            children=[self.question_text, self.input_answer],
        )

        # Boxes
        _box_task = toga.Box(
            children=[BoxFlexRow(), _box_task_inner, BoxFlexRow()]
        )
        _box_panel_result = toga.Box(
            children=[BoxFlexRow(), self.panel_result, BoxFlexRow()]
        )
        _box_btns = toga.Box(children=[BtnBack(), self.btn_submit])

        # DOM
        self.add(
            _box_task,
            _box_panel_result,
            BoxFlexCol(),
            self.num_keyboard,
            _box_btns,
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._contr.on_open(widget)


class FractionExercisePage(FractionLayout):
    """Fraction exercise pages."""

    title = 'Упражнение на дроби'
