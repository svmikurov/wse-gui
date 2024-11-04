"""Application constants."""

from wse.constants.literal import (
    ACTION,
    ALIAS,
    ANSWER,
    ANSWER_TEXT,
    ASSESSMENT,
    AUTH_TOKEN,
    CATEGORIES,
    CATEGORY,
    DETAIL,
    EDGE_PERIODS,
    ERROR,
    EXERCISE_CHOICES,
    FOREIGN_WORD,
    HUMANLY,
    ID,
    ITEMS,
    KNOW,
    LOOKUP_CONDITIONS,
    NAME,
    NEXT,
    NOT_KNOW,
    PASSWORD,
    PERIOD_END,
    PERIOD_START,
    PREVIOUS,
    PROGRESS,
    QUESTION,
    QUESTION_TEXT,
    RESULTS,
    RUSSIAN_WORD,
    STYLE,
    TERM_ID,
    TIMEOUT,
    USERNAME,
)
from wse.constants.page import (
    AUTH_BOX,
    FOREIGN_CREATE_BOX,
    FOREIGN_EXERCISE_BOX,
    FOREIGN_LIST_BOX,
    FOREIGN_MAIN_BOX,
    FOREIGN_PARAMS_BOX,
    FOREIGN_UPDATE_BOX,
    GLOSSARY_CREATE_BOX,
    GLOSSARY_EXERCISE_BOX,
    GLOSSARY_LIST_BOX,
    GLOSSARY_MAIN_BOX,
    GLOSSARY_PARAMS_BOX,
    GLOSSARY_UPDATE_BOX,
    LOGIN_BOX,
    MAIN_BOX,
    USER_CREATE_BOX,
    USER_MAIN_BOX,
    USER_UPDATE_BOX,
)
from wse.constants.settings import (
    BTN_GOTO_FOREIGN_CREATE,
    BTN_GOTO_FOREIGN_LIST,
    BTN_GOTO_FOREIGN_MAIN,
    BTN_GOTO_FOREIGN_PARAMS,
    BTN_GOTO_GLOSSARY_CREATE,
    BTN_GOTO_GLOSSARY_EXERCISE,
    BTN_GOTO_GLOSSARY_LIST,
    BTN_GOTO_GLOSSARY_MAIN,
    BTN_GOTO_GLOSSARY_PARAMS,
    BTN_GOTO_LOGIN,
    BTN_GOTO_MAIN,
    BTN_LOGOUT,
    BUTTON_HEIGHT,
    CONNECTION_ERROR_MSG,
    DEFAULT_TIMEOUT,
    FONT_SIZE_APP,
    INPUT_HEIGHT,
    LOGIN_BAD_MSG,
    LOGIN_MSG,
    LOGOUT_MSG,
    NO_TASK_MSG,
    SCREEN_SIZE,
    TASK_ERROR_MSG,
    TEXT_DISPLAY_FONT_SIZE,
    TEXT_DISPLAY_FONT_STYLE,
    TEXT_DISPLAY_PADDING,
    TITLE_FOREIGN_CREATE,
    TITLE_FOREIGN_EXERCISE,
    TITLE_FOREIGN_LIST,
    TITLE_FOREIGN_MAIN,
    TITLE_FOREIGN_PARAMS,
    TITLE_FOREIGN_UPDATE,
    TITLE_GLOSSARY_CREATE,
    TITLE_GLOSSARY_EXERCISE,
    TITLE_GLOSSARY_LIST,
    TITLE_GLOSSARY_MAIN,
    TITLE_GLOSSARY_PARAMS,
    TITLE_GLOSSARY_UPDATE,
    TITLE_LABEL_FONT_SIZE,
    TITLE_LABEL_HEIGHT,
    TITLE_LABEL_PADDING,
    TITLE_LOGIN,
    TITLE_MAIN,
    TITLE_USER_MAIN,
    TITLE_USER_UPDATE,
    USER_CREATE_MESSAGE,
    USER_UPDATE_MESSAGE,
)
from wse.constants.url import (
    FOREIGN_ASSESSMENT_PATH,
    FOREIGN_DETAIL_PATH,
    FOREIGN_EXERCISE_PATH,
    FOREIGN_PARAMS_PATH,
    FOREIGN_PATH,
    FOREIGN_PROGRESS_PATH,
    GLOSSARY_DETAIL_PATH,
    GLOSSARY_EXERCISE_PATH,
    GLOSSARY_PARAMS_PATH,
    GLOSSARY_PATH,
    GLOSSARY_PROGRESS_PATH,
    HOST_API,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    LOGIN_PATH,
    LOGOUT_PATH,
    RESPONSE_ERROR_MSGS,
    TOKEN_PATH,
    USER_CREATE_PATH,
    USER_ME,
    USER_UPDATE_PATH,
)

__all__ = (  # noqa: F405
    'ACTION',
    'ALIAS',
    'ANSWER',
    'ANSWER_TEXT',
    'ASSESSMENT',
    'AUTH_BOX',
    'AUTH_TOKEN',
    'BTN_GOTO_FOREIGN_CREATE',
    'BTN_GOTO_FOREIGN_LIST',
    'BTN_GOTO_FOREIGN_MAIN',
    'BTN_GOTO_FOREIGN_PARAMS',
    'BTN_GOTO_GLOSSARY_CREATE',
    'BTN_GOTO_GLOSSARY_EXERCISE',
    'BTN_GOTO_GLOSSARY_LIST',
    'BTN_GOTO_GLOSSARY_MAIN',
    'BTN_GOTO_GLOSSARY_PARAMS',
    'BTN_GOTO_LOGIN',
    'BTN_GOTO_MAIN',
    'BTN_LOGOUT',
    'BUTTON_HEIGHT',
    'CATEGORIES',
    'CATEGORY',
    'CONNECTION_ERROR_MSG',
    'DEFAULT_TIMEOUT',
    'DETAIL',
    'EDGE_PERIODS',
    'ERROR',
    'EXERCISE_CHOICES',
    'FONT_SIZE_APP',
    'FOREIGN_ASSESSMENT_PATH',
    'FOREIGN_CREATE_BOX',
    'FOREIGN_DETAIL_PATH',
    'FOREIGN_EXERCISE_BOX',
    'FOREIGN_EXERCISE_PATH',
    'FOREIGN_LIST_BOX',
    'FOREIGN_MAIN_BOX',
    'FOREIGN_PARAMS_BOX',
    'FOREIGN_PARAMS_PATH',
    'FOREIGN_PATH',
    'FOREIGN_PROGRESS_PATH',
    'FOREIGN_UPDATE_BOX',
    'FOREIGN_WORD',
    'GLOSSARY_CREATE_BOX',
    'GLOSSARY_DETAIL_PATH',
    'GLOSSARY_EXERCISE_BOX',
    'GLOSSARY_EXERCISE_PATH',
    'GLOSSARY_LIST_BOX',
    'GLOSSARY_MAIN_BOX',
    'GLOSSARY_PARAMS_BOX',
    'GLOSSARY_PARAMS_PATH',
    'GLOSSARY_PATH',
    'GLOSSARY_PROGRESS_PATH',
    'GLOSSARY_UPDATE_BOX',
    'HOST_API',
    'HTTP_400_BAD_REQUEST',
    'HTTP_401_UNAUTHORIZED',
    'HTTP_500_INTERNAL_SERVER_ERROR',
    'HUMANLY',
    'ID',
    'INPUT_HEIGHT',
    'ITEMS',
    'KNOW',
    'LOGIN_BAD_MSG',
    'LOGIN_BOX',
    'LOGIN_MSG',
    'LOGIN_PATH',
    'LOGOUT_MSG',
    'LOGOUT_PATH',
    'LOOKUP_CONDITIONS',
    'MAIN_BOX',
    'NAME',
    'NEXT',
    'NOT_KNOW',
    'NO_TASK_MSG',
    'PASSWORD',
    'PERIOD_END',
    'PERIOD_START',
    'PREVIOUS',
    'PROGRESS',
    'QUESTION',
    'QUESTION_TEXT',
    'RESPONSE_ERROR_MSGS',
    'RESULTS',
    'RUSSIAN_WORD',
    'SCREEN_SIZE',
    'STYLE',
    'TASK_ERROR_MSG',
    'TERM_ID',
    'TEXT_DISPLAY_FONT_SIZE',
    'TEXT_DISPLAY_FONT_STYLE',
    'TEXT_DISPLAY_PADDING',
    'TIMEOUT',
    'TITLE_FOREIGN_CREATE',
    'TITLE_FOREIGN_EXERCISE',
    'TITLE_FOREIGN_LIST',
    'TITLE_FOREIGN_MAIN',
    'TITLE_FOREIGN_PARAMS',
    'TITLE_FOREIGN_UPDATE',
    'TITLE_GLOSSARY_CREATE',
    'TITLE_GLOSSARY_EXERCISE',
    'TITLE_GLOSSARY_LIST',
    'TITLE_GLOSSARY_MAIN',
    'TITLE_GLOSSARY_PARAMS',
    'TITLE_GLOSSARY_UPDATE',
    'TITLE_LABEL_FONT_SIZE',
    'TITLE_LABEL_HEIGHT',
    'TITLE_LABEL_PADDING',
    'TITLE_LOGIN',
    'TITLE_MAIN',
    'TITLE_USER_MAIN',
    'TITLE_USER_UPDATE',
    'TOKEN_PATH',
    'USERNAME',
    'USER_CREATE_BOX',
    'USER_CREATE_MESSAGE',
    'USER_CREATE_PATH',
    'USER_MAIN_BOX',
    'USER_ME',
    'USER_UPDATE_BOX',
    'USER_UPDATE_MESSAGE',
    'USER_UPDATE_PATH',
)
