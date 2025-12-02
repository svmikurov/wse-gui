"""Foreign discipline fixtures."""

from dataclasses import fields
from typing import Final

from tests import types
from wse.data.dto import foreign as dto
from wse.data.schemas import foreign as schemas

# Data
# ~~~~


TRANSLATE_ORDER_OPTIONS: Final[list[types.CodeNameT]] = [
    {'code': 'from_native', 'name': 'С родного языка'},
    {'code': 'to_native', 'name': 'На родной язык'},
    {'code': 'random', 'name': 'Случайный порядок'},
]

OPTIONS: Final[types.PresentationOptionsT] = {
    'categories': [
        {'id': 1, 'name': 'category 1'},
        {'id': 2, 'name': 'category 2'},
    ],
    'marks': [
        {'id': 1, 'name': 'mark 1'},
        {'id': 2, 'name': 'mark'},
    ],
    'sources': [
        {'id': 1, 'name': 'source 1'},
        {'id': 2, 'name': 'source 2'},
    ],
    'periods': [
        {'id': 1, 'name': 'today'},
        {'id': 2, 'name': 'week_before'},
    ],
    'translation_orders': TRANSLATE_ORDER_OPTIONS,
}

SELECTED: Final[types.SelectedParametersT] = {
    'category': OPTIONS['categories'][1],
    'mark': OPTIONS['marks'][1],
    'word_source': OPTIONS['sources'][1],
    'start_period': OPTIONS['periods'][1],
    'end_period': OPTIONS['periods'][1],
    'translation_order': TRANSLATE_ORDER_OPTIONS[1],
}

SETTINGS: Final[types.PresentationSettingsT] = {
    'word_count': 90,
    'question_timeout': 2,
    'answer_timeout': 2,
}

CHANGED: Final[types.InitialParametersT] = {
    'category': OPTIONS['categories'][0],
    'mark': OPTIONS['marks'][0],
    'word_source': OPTIONS['sources'][0],
    'start_period': OPTIONS['periods'][0],
    'end_period': OPTIONS['periods'][0],
    'translation_order': TRANSLATE_ORDER_OPTIONS[0],
    'word_count': 70,
    'question_timeout': 1,
    'answer_timeout': 1,
}


# HTTP payload
# ~~~~~~~~~~~~


# TODO: Apply typed dict
PARAMETERS_RESPONSE_PAYLOAD: Final = {
    'status': 'success',
    'code': 200,
    'message': 'Success',
    'data': {**OPTIONS, **SELECTED, **SETTINGS},
}

# TODO: Apply typed dict
PRESENTATION_REQUEST_PAYLOAD: Final = {
    # Selected options
    'category': SELECTED['category'],
    'mark': SELECTED['mark'],
    'word_source': SELECTED['word_source'],
    'translation_order': SELECTED['translation_order'],
    'start_period': SELECTED['start_period'],
    'end_period': SELECTED['end_period'],
    # Set options
    'word_count': SETTINGS['word_count'],
}

# TODO: Apply typed dict
PRESENTATION_RESPONSE_PAYLOAD: Final = {
    'status': 'success',
    'code': 200,
    'message': 'Success',
    'data': {
        'case_uuid': '75c77f0c-9475-48a6-a352-c3968cef15ac',
        'definition': 'word',
        'explanation': 'слово',
        'info': {
            'progress': 4,
        },
    },
}


# Schemas
# ~~~~~~~


INITIAL_PARAMETERS_SCHEMA: Final = schemas.InitialParameters.from_dict(
    {**SELECTED, **SETTINGS},
)


PARAMETERS_SCHEMA: Final = schemas.PresentationParameters.from_dict(
    {**OPTIONS, **SELECTED, **SETTINGS},
)


# DTO
# ~~~

INITIAL_PARAMETERS_DTO: Final = dto.InitialParameters(
    category=dto.IdName(**SELECTED['category']),  # type: ignore[arg-type]
    mark=dto.IdName(**SELECTED['mark']),  # type: ignore[arg-type]
    word_source=dto.IdName(**SELECTED['word_source']),  # type: ignore[arg-type]
    translation_order=dto.CodeName(**SELECTED['translation_order']),  # type: ignore[arg-type]
    start_period=dto.IdName(**SELECTED['start_period']),  # type: ignore[arg-type]
    end_period=dto.IdName(**SELECTED['end_period']),  # type: ignore[arg-type]
    **SETTINGS,
)

CHANGED_PARAMETERS_DTO: Final = dto.InitialParameters(
    category=dto.IdName(**CHANGED['category']),  # type: ignore[arg-type]
    mark=dto.IdName(**CHANGED['mark']),  # type: ignore[arg-type]
    word_source=dto.IdName(**CHANGED['word_source']),  # type: ignore[arg-type]
    translation_order=dto.CodeName(**CHANGED['translation_order']),  # type: ignore[arg-type]
    start_period=dto.IdName(**CHANGED['start_period']),  # type: ignore[arg-type]
    end_period=dto.IdName(**CHANGED['end_period']),  # type: ignore[arg-type]
    word_count=CHANGED['word_count'],
    question_timeout=CHANGED['question_timeout'],
    answer_timeout=CHANGED['answer_timeout'],
)

PARAMETERS_DTO: Final = dto.PresentationParameters(
    categories=[dto.IdName(**items) for items in OPTIONS['categories']],
    marks=[dto.IdName(**items) for items in OPTIONS['marks']],
    sources=[dto.IdName(**items) for items in OPTIONS['sources']],
    periods=[dto.IdName(**items) for items in OPTIONS['periods']],
    translation_orders=[
        dto.CodeName(**items) for items in OPTIONS['translation_orders']
    ],
    **{
        field.name: getattr(INITIAL_PARAMETERS_DTO, field.name)
        for field in fields(INITIAL_PARAMETERS_DTO)
    },
)
