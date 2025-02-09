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

    foreign_main = {
        'text': 'Иностранный',
        'on_press': gh.goto_foreign_main,
    }
    foreign_create = {
        'text': 'Добавить слово',
        'on_press': gh.goto_foreign_create,
    }
    foreign_params = {
        'text': 'Изучение слов',
        'on_press': gh.goto_foreign_params,
    }
    foreign_tasks = {
        'text': 'Выполнение заданий',
        'on_press': gh.goto_foreign_tasks,
    }
    foreign_test = {
        'text': 'Тест',
        'on_press': gh.goto_foreign_test,
    }

    ####################################################################
    # Glossary

    glossary_main = {
        'text': 'Глоссарий',
        'on_press': gh.goto_glossary_main,
    }
    glossary_params = {
        'text': 'Изучение терминов',
        'on_press': gh.goto_glossary_params,
    }
    glossary_create = {
        'text': 'Добавить термин',
        'on_press': gh.goto_glossary_create,
    }

    ####################################################################
    # Mathematics

    math_main = {
        'text': 'Математика',
        'on_press': gh.goto_math_main,
    }
    calculations = {
        'text': 'Упражнение на вычисления',
        'on_press': gh.goto_calc_exercise,
    }
    fractions = {
        'text': 'Упражнения с дробями',
        'on_press': gh.goto_fraction_exercise,
    }

    ####################################################################
    # Mentoring

    mentoring = {
        'text': 'Выполнение заданий',
        'on_press': gh.goto_mentoring,
    }
    word_test = {
        'text': 'Тест по иностранному языку',
        'on_press': gh.goto_word_test,
    }

    ####################################################################
    # Explorer

    explorer_main = {'text': 'Изучение виджетов', 'on_press': gh.goto_explorer}
