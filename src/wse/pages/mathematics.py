"""Mathematical exercise pages."""

from wse.pages.containers.fraction import FractionLayout
from wse.pages.handlers.goto_handler import (
    goto_calculations_exercise,
    goto_fraction_exercise_handler,
    goto_multiplication_exercise_handler,
)
from wse.pages.widgets.box import BoxFlexRow
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp, BtnBack
from wse.pages.widgets.label import TitleLabel


class MathematicalMainPage(BaseBox):
    """Mathematical exercises main pages."""

    title = 'Упражнения по математике'

    def __init__(self) -> None:
        """Construct the pages."""
        super().__init__()
        _label_title = TitleLabel(text=self.title)

        _btn_goto_multiplication = BtnApp(
            'Таблица умножения', on_press=goto_multiplication_exercise_handler
        )
        _btn_goto_calculations = BtnApp(
            'Упражнение на вычисления', on_press=goto_calculations_exercise
        )
        _btn_goto_fraction = BtnApp(
            'Упражнения с дробями', on_press=goto_fraction_exercise_handler
        )

        # DOM
        self.add(
            _label_title,
            BoxFlexRow(),
            _btn_goto_multiplication,
            _btn_goto_calculations,
            _btn_goto_fraction,
            BtnBack(),
        )


class FractionExercisePage(FractionLayout):
    """Fraction exercise pages."""

    title = 'Упражнение на дроби'
