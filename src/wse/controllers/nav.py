"""Moving to page controller."""

from typing import Callable

from wse.pages.handlers.goto_handler import (
    goto_explorer,
    goto_foreign_main,
    goto_glossary_main,
    goto_login,
    goto_math_main,
    goto_mentoring,
)


class Navigation:
    """Moving to page the button controller."""

    @staticmethod
    def _create_attrs(text: str, on_press: Callable) -> dict:
        """Return the button named attributes."""
        return {'text': text, 'on_press': on_press}

    ####################################################################
    # Navigation targets                                               #
    ####################################################################

    @property
    def login(self) -> dict:
        """The attrs of button go to login page."""
        return self._create_attrs('Вход в учетную запись', goto_login)

    ####################################################################
    # Foreign

    @property
    def foreign_main(self) -> dict:
        """The attrs of button go to foreign main page."""
        return self._create_attrs('Иностранный', goto_foreign_main)

    ####################################################################
    # Glossary

    @property
    def glossary_main(self) -> dict:
        """The attrs of button go to glossary main page."""
        return self._create_attrs('Глоссарий', goto_glossary_main)

    ####################################################################
    # Mathematics

    @property
    def math_main(self) -> dict:
        """The attrs of button go to mathematics main page."""
        return self._create_attrs('Математика', goto_math_main)

    ####################################################################
    # Mentoring

    @property
    def mentoring(self) -> dict:
        """The attrs of button go to mentoring main page."""
        return self._create_attrs('Выполнение заданий', goto_mentoring)

    ####################################################################
    # Explorer

    @property
    def explorer_main(self) -> dict:
        """The attrs of button go to Toga explorer main page."""
        return self._create_attrs('Изучение виджетов', goto_explorer)
