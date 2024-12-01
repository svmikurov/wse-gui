"""App boxes to assign to window content."""

from wse.pages.foreign import (
    CreateWordPage,
    ExerciseForeignPage,
    ListForeignPage,
    MainForeignWidget,
    ParamsForeignPage,
    UpdateWordPage,
)
from wse.pages.glossary import (
    CreateTermPage,
    ExerciseGlossaryPage,
    ListGlossaryPage,
    MainGlossaryWidget,
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
    'MainForeignWidget',
    'MainGlossaryWidget',
    'ParamsForeignPage',
    'ParamsGlossaryPage',
    'UpdateWordPage',
    'UpdateTermPage',
)
