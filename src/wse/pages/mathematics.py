"""Mathematical exercise pages."""

from wse.pages.containers.fraction import FractionLayout
from wse.pages.containers.multiplication import MultiplicationWidgets
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_fraction_exercise_handler,
    goto_multiplication_exercise_handler,
)
from wse.pages.widgets.box import BoxFlexRow
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel


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


class MultiplicationExercisePage(MultiplicationWidgets):
    """Multiplication exercise page."""

    title = 'Таблица умножения'


class FractionExercisePage(FractionLayout):
    """Fraction exercise page."""

    title = 'Упражнение на дроби'
