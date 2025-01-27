"""The application url endpoints."""

from http import HTTPStatus

# HOST = 'http://127.0.0.1/'
HOST = 'http://wselfedu.online/'
"""Host to connect (`str`).
"""

LOGIN_PATH = '/auth/token/login/'
"""User login url path, allowed POST method (`str`).
"""
LOGOUT_PATH = '/auth/token/logout/'
"""User logout url path, allowed POST method (`str`).
"""
USER_CREATE_PATH = '/api/v1/auth/users/'
"""User registration path, allowed POST method (`str`).
"""
USER_DETAIL = '/api/v1/auth/users/%s/'
"""User detail endpoint, allowed GET method (`str`).
"""
USER_UPDATE_PATH = '/api/v1/auth/users/set_username/'
"""User update endpoint, allowed POST method (`str`).
"""
USER_ME_PATH = '/api/v1/auth/users/me/'
"""User detail endpoint, allowed GET method (`str`).
"""
TOKEN_PATH = '/auth/token/login/'
"""Endpoint to obtain the user auth token, allowed method: POST (`str`).
"""

FOREIGN_EXERCISE_PATH = '/api/v1/foreign/exercise/'
"""Learning foreign word exercise path (`str`).
"""
FOREIGN_ASSESSMENT_PATH = '/api/v1/foreign/progress/'
"""User knowledge assessment update of foreign word path (`str`).
"""
FOREIGN_PROGRESS_PATH = '/api/v1/foreign/progress/'
"""Learning foreign word progress path (`str`).
"""
FOREIGN_PARAMS_PATH = '/api/v1/foreign/params/'
"""Learning foreign word exercise parameters path (`str`).
"""
FOREIGN_PATH = '/api/v1/foreign/'
"""Create foreign word and list of foreign word the url path(`str`).
"""
FOREIGN_SELECTED_PATH = '/api/v1/foreign/selected/'
"""Selected foreign words the url path(`str`).
"""
FOREIGN_FAVORITES_PATH = '/api/v1/foreign/favorites/'
"""Update word favorites status the url path(`str`).
"""
FOREIGN_DETAIL_PATH = '/api/v1/foreign/%s/'
"""Detail foreign word the url path(`str`).
"""

GLOSSARY_EXERCISE_PATH = '/api/v1/glossary/exercise/'
"""Glossary exercise path (`str`).
"""
GLOSSARY_FAVORITES_PATH = '/api/v1/glossary/favorites/'
"""Update term favorites status the url path(`str`).
"""
GLOSSARY_PARAMS_PATH = '/api/v1/glossary/params/'
"""Glossary exercise parameters path (`str`).
"""
GLOSSARY_PROGRESS_PATH = '/api/v1/glossary/progress/'
"""Glossary progress update path (`str`).
"""
GLOSSARY_DETAIL_PATH = '/api/v1/glossary/%s/'
"""Detail glossary term the url path(`str`).
"""
GLOSSARY_PATH = '/api/v1/glossary/'
"""Create and list of glossary term the url path(`str`).
"""
GLOSSARY_SELECTED_PATH = '/api/v1/glossary/selected/'
"""Selected glossary terms the url path(`str`).
"""

HTTP_400_BAD_REQUEST = HTTPStatus.BAD_REQUEST
HTTP_401_UNAUTHORIZED = HTTPStatus.UNAUTHORIZED
HTTP_500_INTERNAL_SERVER_ERROR = HTTPStatus.INTERNAL_SERVER_ERROR

RESPONSE_ERROR_MSGS = {
    HTTP_400_BAD_REQUEST: ('', 'Предоставлены неверные данные'),
    HTTP_401_UNAUTHORIZED: ('', 'Необходимо авторизоваться'),
    HTTP_500_INTERNAL_SERVER_ERROR: ('', 'Ошибка сервера'),
}
