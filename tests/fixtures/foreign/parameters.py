"""Foreign discipline data fixtures."""

from tests import types
from wse.api.foreign import requests, schemas
from wse.api.schemas import base as base_schemas

# Data
# ~~~~


TRANSLATE_ORDER_OPTIONS: list[types.CodeNameT] = [
    {'code': 'from_native', 'name': 'С родного языка'},
    {'code': 'to_native', 'name': 'На родной язык'},
    {'code': 'random', 'name': 'Случайный порядок'},
]

PRESENTATION_OPTIONS: types.ParamOptionsT = {
    'categories': [
        {'id': 1, 'name': 'cat 1'},
        {'id': 2, 'name': 'cat 2'},
    ],
    'marks': [
        {'id': 1, 'name': 'mark 1'},
        {'id': 2, 'name': 'mark'},
    ],
    'sources': [
        {'id': 1, 'name': 'source 1'},
    ],
    'periods': [
        {'id': 1, 'name': 'today'},
        {'id': 2, 'name': 'week_before'},
    ],
    'translation_orders': TRANSLATE_ORDER_OPTIONS,
}

PRESENTATION_SETTINGS: types.PresentationSettingsT = {
    'word_count': 90,
    'question_timeout': 2.0,
    'answer_timeout': 2.5,
}


# Schemas
# ~~~~~~~

PRESENTATION_PARAMETERS_SCHEMA = schemas.PresentationParams(
    categories=[
        base_schemas.IdNameSchema(id=1, name='category 1'),
        base_schemas.IdNameSchema(id=2, name='category 2'),
    ],
    marks=[
        base_schemas.IdNameSchema(id=1, name='mark 1'),
        base_schemas.IdNameSchema(id=2, name='mark 2'),
    ],
    sources=[
        base_schemas.IdNameSchema(id=1, name='source 1'),
        base_schemas.IdNameSchema(id=2, name='source 2'),
    ],
    periods=[
        base_schemas.IdNameSchema(id=1, name='start period'),
        base_schemas.IdNameSchema(id=2, name='end period'),
    ],
    translation_orders=[
        base_schemas.CodeNameSchema(code='to_native', name='To native'),
        base_schemas.CodeNameSchema(code='from_native', name='From native'),
        base_schemas.CodeNameSchema(code='random', name='Random'),
    ],
    category=base_schemas.IdNameSchema(id=1, name='category 1'),
    mark=base_schemas.IdNameSchema(id=2, name='mark 2'),
    word_source=base_schemas.IdNameSchema(id=2, name='source 2'),
    translation_order=base_schemas.CodeNameSchema(
        code='to_native', name='To native'
    ),
    word_count=78,
    question_timeout=2,
    answer_timeout=3,
    start_period=base_schemas.IdNameSchema(id=1, name='start period'),
    end_period=base_schemas.IdNameSchema(id=2, name='end period'),
)


# DTO
# ~~~


PRESENTATION_PARAMETERS_DTO = requests.PresentationParamsDTO(
    categories=[
        requests.IdName(id=1, name='category 1'),
        requests.IdName(id=2, name='category 2'),
    ],
    marks=[
        requests.IdName(id=1, name='mark 1'),
        requests.IdName(id=2, name='mark 2'),
    ],
    sources=[
        requests.IdName(id=1, name='source 1'),
        requests.IdName(id=2, name='source 2'),
    ],
    periods=[
        requests.IdName(id=1, name='start period'),
        requests.IdName(id=2, name='end period'),
    ],
    translation_orders=[
        requests.CodeName(code='to_native', name='To native'),
        requests.CodeName(code='from_native', name='From native'),
        requests.CodeName(code='random', name='Random'),
    ],
    category=requests.IdName(id=1, name='category 1'),
    mark=requests.IdName(id=2, name='mark 2'),
    word_source=requests.IdName(id=2, name='source 2'),
    translation_order=requests.CodeName(code='to_native', name='To native'),
    question_timeout=2,
    answer_timeout=3,
    start_period=requests.IdName(id=1, name='start period'),
    end_period=requests.IdName(id=2, name='end period'),
    word_count=78,
)
