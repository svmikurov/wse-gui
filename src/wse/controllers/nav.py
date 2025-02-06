"""Moving to page controller."""

from typing import Callable

from wse.pages.handlers import goto_handler as gh


class Navigation:
    """Moving to page the button controller."""

    __instance = None

    def __new__(cls) -> None:
        """Create single instance."""
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        """Construct the navigation."""
        pass

    def __del__(self) -> None:
        """Delete the class instance."""
        Navigation.__instance = None

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
        return self._create_attrs('Вход в учетную запись', gh.goto_login)

    ####################################################################
    # Foreign

    @property
    def foreign_main(self) -> dict:
        """The attrs of button go to foreign main page."""
        return self._create_attrs('Иностранный', gh.goto_foreign_main)

    ####################################################################
    # Glossary

    @property
    def glossary_main(self) -> dict:
        """The attrs of button go to glossary main page."""
        return self._create_attrs('Глоссарий', gh.goto_glossary_main)

    ####################################################################
    # Mathematics

    @property
    def math_main(self) -> dict:
        """The attrs of button go to mathematics main page."""
        return self._create_attrs('Математика', gh.goto_math_main)

    ####################################################################
    # Mentoring

    @property
    def mentoring(self) -> dict:
        """The attrs of button go to mentoring main page."""
        return self._create_attrs('Выполнение заданий', gh.goto_mentoring)

    ####################################################################
    # Explorer

    @property
    def explorer_main(self) -> dict:
        """The attrs of button go to Toga explorer main page."""
        return self._create_attrs('Изучение виджетов', gh.goto_explorer)
