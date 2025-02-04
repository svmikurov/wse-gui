"""Mathematical exercise page."""

from wse.page.containers.fraction import FractionLayout
from wse.page.containers.multiplication import MultiplicationWidgets
from wse.page.handlers.goto_handler import (
    goto_back_handler,
    goto_fraction_exercise_handler,
    goto_multiplication_exercise_handler,
)
from wse.page.widgets.box import BoxFlexRow
from wse.page.widgets.box_page import BaseBox
from wse.page.widgets.button import BtnApp
from wse.page.widgets.label import TitleLabel


class MathematicalMainPage(BaseBox):
    """Mathematical exercises main page."""

    title = 'Упражнения по математике'

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        _label_title = TitleLabel(text=self.title)

        _box_align = BoxFlexRow()

        _btn_goto_multiplication = BtnApp(
            'Таблица умножения', on_press=goto_multiplication_exercise_handler
        )
        _btn_goto_fraction = BtnApp(
            'Упражнения с дробями', on_press=goto_fraction_exercise_handler
        )
        _btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # DOM
        self.add(
            _label_title,
            _box_align,
            _btn_goto_multiplication,
            _btn_goto_fraction,
            _btn_goto_back,
        )


class MultPage(MultiplicationWidgets):
    """Multiplication exercise page."""

    title = 'Таблица умножения'


class FractionExercisePage(FractionLayout):
    """Fraction exercise page."""

    title = 'Упражнение на дроби'
