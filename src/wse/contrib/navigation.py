"""Navigation buttons attributes."""

from typing import Callable

from wse.pages.handlers import goto_handler as gh


# TODO: Add programmatically creation of button callbacks.
class NavigationAttrs:
    """Navigation buttons attributes."""

    @classmethod
    def set(cls, attr_name: str, text: str, callback: Callable) -> None:
        """Set button attrs."""
        btn_attrs = {'text': text, 'on_press': callback}
        setattr(cls, attr_name, btn_attrs)


nav = NavigationAttrs()

########################################################################
# Main

nav.set('login', 'Вход в учетную запись', gh.goto_login)

########################################################################
# Foreign

nav.set('foreign_main', 'Иностранный', gh.goto_foreign_main)
nav.set('foreign_create', 'Добавить слово', gh.goto_foreign_create)
nav.set('foreign_params', 'Изучение слов', gh.goto_foreign_params)
nav.set('foreign_tasks', 'Выполнение заданий', gh.goto_foreign_tasks)
nav.set('foreign_test', 'Тест', gh.goto_foreign_test)

########################################################################
# Glossary

nav.set('glossary_main', 'Глоссарий', gh.goto_glossary_main)
nav.set('glossary_create', 'Добавить термин', gh.goto_glossary_create)
nav.set('glossary_params', 'Изучение терминов', gh.goto_glossary_params)

########################################################################
# Mathematics

nav.set('math_main', 'Математика', gh.goto_math_main)
nav.set('calculations', 'Упражнение на вычисления', gh.goto_calc_exercise)
nav.set('fractions', 'Упражнения с дробями', gh.goto_fraction_exercise)

########################################################################
# Mentoring

nav.set('mentoring', 'Выполнение заданий', gh.goto_mentoring)
nav.set('word_test', 'Тест по иностранному языку', gh.goto_word_test)

########################################################################
# Explorer

nav.set('explorer_main', 'Изучение виджетов', gh.goto_explorer)
