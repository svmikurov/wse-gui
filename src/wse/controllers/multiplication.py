"""Multiplication exercise controller."""

from typing import TypeVar

import toga
from toga.sources import Source

from wse.controllers.base import BaseContr

ModelT = TypeVar('ModelT', bound=Source)
ViewT = TypeVar('ViewT', bound=toga.Box)


class MultContr(BaseContr):
    """Multiplication exercise controller."""

    def __init__(self, model: ModelT, view: ViewT) -> None:
        """Construct ht controller."""
        super().__init__(model, view)
        self._model = model
        self._model.add_listener(self)
        self._view = view
        self._view.set_controller(self)

        self._view.btn_submit.on_press = self.check_user_answer
        self._view.num_keyboard.add_listener(self)

    async def on_open(self, _: toga.Widget) -> None:
        """Invoke methods on pages open."""
        self.clear()
        await self._model.start_new_task()

    ####################################################################
    # Listener methods

    def clear(self) -> None:
        """Clear previous values of widgets."""
        self._clear_question()
        self._clear_user_answer()
        self._clear_result()

    def display_question(self, text: str) -> None:
        """Display the task question."""
        question = f'{text} = '
        self._view.question_text.text = question

    def update_num_panel(self, text: str) -> None:
        """Update the current user answer."""
        self._model.update_user_answer(text)
        self._clear_result()

    def display_user_answer(self, text: str) -> None:
        """Set the current user answer."""
        self._view.input_answer.text = text

    def display_result(self, text: str) -> None:
        """Display answer result."""
        self._view.panel_result.text = text

    ####################################################################
    # Button callback functions

    async def check_user_answer(self, _: toga.Widget) -> None:
        """Submit answer, button handler."""
        await self._model.check_user_answer()

    ####################################################################
    # Utility methods

    def _clear_user_answer(self) -> None:
        self._view.num_keyboard.clean()
        self.display_user_answer('?')

    def _clear_question(self) -> None:
        self._view.question_text.text = ''

    def _clear_result(self) -> None:
        self.display_result('')
