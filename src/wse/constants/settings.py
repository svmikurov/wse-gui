"""The application widget settings constants."""

from toga import colors
from toga.style import Pack
from travertino.constants import ITALIC

DEFAULT_TIMEOUT = 5
"""Time to answer on task question in exercises (`int`).
"""

########################################################################
# Widget constants
########################################################################

PIXEL_DESKTOP = 1 / 96
PIXEL_PHONE = 1 / 160
PHONE_SCALING = PS = 1 / (PIXEL_PHONE / PIXEL_DESKTOP)

SCREEN_SIZE = (440, 700)
PADDING_NO = 0
PADDING_SM = 2
PADDING_SIDE = (PADDING_NO, PADDING_SM, PADDING_NO, PADDING_SM)
PADDING_AROUND_WIDGET = (PADDING_SM, PADDING_SM, PADDING_SM, PADDING_SM)
FONT_SIZE_APP = 11
BUTTON_HEIGHT = 60
INPUT_HEIGHT = 60
MAX_LINE_LENGTH = 23
"""Max length of table line length (`int`)
"""

STYLE_BTN_CANCEL = Pack(background_color=colors.TOMATO)
STYLE_BTN_CONFIRM = Pack(background_color=colors.GREEN)

#########################################################################
# TextDisplay

TEXT_DISPLAY_FONT_SIZE = 18
TEXT_DISPLAY_FONT_STYLE = ITALIC
TEXT_DISPLAY_PADDING = (0, 2, 0, 2)

#########################################################################
# Titles

TITLE_LABEL_FONT_SIZE = 16
TITLE_LABEL_HEIGHT = 35
TITLE_LABEL_PADDING = (5, 0, 10, 0)
# Main
TITLE_MAIN = 'WSELFEDU'
BTN_GOTO_MAIN = 'На главную'
# User
TITLE_LOGIN = 'Вход в учетную запись'
TITLE_USER_MAIN = 'Учетная запись'
TITLE_USER_UPDATE = 'Изменить имя'
TITLE_USER_CREATE = 'Регистрация'
BTN_GOTO_LOGIN = 'Вход в учетную запись'
BTN_LOGIN = 'Войти в учетную запись'
BTN_LOGOUT = 'Выйти из учетной записи'
# Glossary
TITLE_GLOSSARY_MAIN = 'Глоссарий'
TITLE_GLOSSARY_CREATE = 'Добавить термин'
TITLE_GLOSSARY_UPDATE = 'Изменить термин'
TITLE_GLOSSARY_LIST = 'Список терминов'
TITLE_GLOSSARY_PARAMS = 'Параметры изучения терминов'
TITLE_GLOSSARY_EXERCISE = 'Изучение терминов'
BTN_GOTO_GLOSSARY_MAIN = 'Глоссарий'
BTN_GOTO_GLOSSARY_LIST = 'Словарь терминов'
BTN_GOTO_GLOSSARY_EXERCISE = 'Начать упражнение'
BTN_GOTO_GLOSSARY_PARAMS = 'Изучение терминов'
BTN_GOTO_GLOSSARY_CREATE = 'Добавить термин'
# Foreign
TITLE_FOREIGN_MAIN = 'Иностранный язык'
TITLE_FOREIGN_CREATE = 'Добавить слово'
TITLE_FOREIGN_UPDATE = 'Изменить термин'
TITLE_FOREIGN_LIST = 'Словарь иностранных слов'
TITLE_FOREIGN_PARAMS = 'Параметры изучения слов'
TITLE_FOREIGN_EXERCISE = 'Изучение иностранных слов'
TITLE_FOREIGN_TASKS = 'Задания по Иностранному языку'
TITLE_FOREIGN_TEST = 'Тест по Иностранному языку'
BTN_GOTO_FOREIGN_MAIN = 'Иностранный'
BTN_GOTO_FOREIGN_CREATE = 'Добавить слово'
BTN_GOTO_FOREIGN_LIST = 'Словарь иностранных слов'
BTN_GOTO_FOREIGN_EXERCISE = 'Начать упражнение'
BTN_GOTO_FOREIGN_PARAMS = 'Изучение слов'
BTN_GOTO_FOREIGN_TASKS = 'Выполнение заданий'

#########################################################################
# Messages

LOGIN_MSG = 'Вы вошли в учетную записи'
LOGIN_BAD_MSG = 'Неверный логин или пароль'
LOGOUT_MSG = 'Вы вышли из учетной записи'
USER_CREATE_MESSAGE = 'Вы создали учетную запись'
USER_UPDATE_MESSAGE = 'Вы изменили имя'
CONNECTION_SUCCESS_MSG = ('Подключение:', 'соединение установлено')
CONNECTION_BAD_MSG = ('Подключение:', 'неверный логин или пароль')
CONNECTION_ERROR_MSG = ('Подключение:', 'в соединении отказано')
NO_TASK_MSG = 'По заданным условия задание не сформировано'
TASK_ERROR_MSG = 'Ошибка формирования задания'
