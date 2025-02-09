"""Moving to page, the controller."""

from typing import Callable

from wse.contrib.singelton import Singleton
from wse.pages.handlers import goto_handler as gh


# TODO: Refactor: Add programming creation of button callbacks.
class Navigation(Singleton):
    """Moving to page the button controller."""

    def add(self, attr_name: str, text: str, callback: Callable) -> None:
        """Add button attrs for navigation."""
        btn_attrs = {'text': text, 'on_press': callback}
        setattr(self, attr_name, btn_attrs)


nav = Navigation()

####################################################################
# Main

nav.add('login', 'Вход в учетную запись', gh.goto_login)

########################################################################
# Foreign

nav.add('foreign_main', 'Иностранный', gh.goto_foreign_main)
nav.add('foreign_create', 'Добавить слово', gh.goto_foreign_create)
nav.add('foreign_params', 'Изучение слов', gh.goto_foreign_params)
nav.add('foreign_tasks', 'Выполнение заданий', gh.goto_foreign_tasks)
nav.add('foreign_test', 'Тест', gh.goto_foreign_test)

####################################################################
# Glossary

nav.add('glossary_main', 'Глоссарий', gh.goto_glossary_main)
nav.add('glossary_create', 'Добавить термин', gh.goto_glossary_create)
nav.add('glossary_params', 'Изучение терминов', gh.goto_glossary_params)

########################################################################
# Mathematics

nav.add('math_main', 'Математика', gh.goto_math_main)
nav.add('calculations', 'Упражнение на вычисления', gh.goto_calc_exercise)
nav.add('fractions', 'Упражнения с дробями', gh.goto_fraction_exercise)

########################################################################
# Mentoring

nav.add('mentoring', 'Выполнение заданий', gh.goto_mentoring)
nav.add('word_test', 'Тест по иностранному языку', gh.goto_word_test)

########################################################################
# Explorer

nav.add('explorer_main', 'Изучение виджетов', gh.goto_explorer)
