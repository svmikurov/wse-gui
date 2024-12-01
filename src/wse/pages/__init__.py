"""App boxes to assign to window content."""

from wse.pages.foreign import (
    CreateWordPage,
    ExerciseForeignPage,
    ListForeignPage,
    MainForeignPage,
    ParamsForeignPage,
    UpdateWordPage,
)
from wse.pages.glossary import (
    CreateTermPage,
    ExerciseGlossaryPage,
    ListGlossaryPage,
    MainGlossaryPage,
    ParamsGlossaryPage,
    UpdateTermPage,
)
from wse.pages.login import LoginBox
from wse.pages.main import (
    MainBox,
)

__all__ = (
    'CreateWordPage',
    'CreateTermPage',
    'ExerciseGlossaryPage',
    'ExerciseForeignPage',
    'ListForeignPage',
    'ListGlossaryPage',
    'LoginBox',
    'MainBox',
    'MainForeignPage',
    'MainGlossaryPage',
    'ParamsForeignPage',
    'ParamsGlossaryPage',
    'UpdateWordPage',
    'UpdateTermPage',
)
