"""Moving to page controller."""

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

    ####################################################################
    # Main

    login = {'text': 'Вход в учетную запись', 'on_press': gh.goto_login}

    ####################################################################
    # Foreign

    foreign_main = {'text': 'Иностранный', 'on_press': gh.goto_foreign_main}

    ####################################################################
    # Glossary

    glossary_main = {'text': 'Глоссарий', 'on_press': gh.goto_glossary_main}

    ####################################################################
    # Mathematics

    math_main = {
        'text': 'Математика',
        'on_press': gh.goto_math_main,
    }
    calculations = {
        'text': 'Упражнение на вычисления',
        'on_press': gh.goto_calculations_exercise,
    }
    fractions = {
        'text': 'Упражнения с дробями',
        'on_press': gh.goto_fraction_exercise,
    }

    ####################################################################
    # Mentoring

    mentoring = {'text': 'Выполнение заданий', 'on_press': gh.goto_mentoring}

    ####################################################################
    # Explorer

    explorer_main = {'text': 'Изучение виджетов', 'on_press': gh.goto_explorer}
