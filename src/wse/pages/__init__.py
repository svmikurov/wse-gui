"""App boxes to assign to window content."""

from wse.pages.examples.explorer import ExplorerLayout
from wse.pages.foreign import (
    CreateWordPage,
    ExerciseForeignPage,
    MainForeignPage,
    ParamsForeignPage,
    TableWordPage,
    TasksForeignPage,
    TestForeignPage,
    UpdateWordPage,
)
from wse.pages.glossary import (
    CreateTermPage,
    ExerciseGlossaryPage,
    MainGlossaryWidget,
    ParamsGlossaryPage,
    TableTermPage,
    UpdateTermPage,
)
from wse.pages.login import LoginBox
from wse.pages.main import MainBox
from wse.pages.mentoring import (
    MentoringPage,
)

__all__ = (
    'CreateTermPage',
    'CreateWordPage',
    'ExerciseForeignPage',
    'ExerciseGlossaryPage',
    'ExplorerLayout',
    'LoginBox',
    'MainBox',
    'MainForeignPage',
    'MainGlossaryWidget',
    'MentoringPage',
    'ParamsForeignPage',
    'ParamsGlossaryPage',
    'TableTermPage',
    'TableWordPage',
    'TasksForeignPage',
    'TestForeignPage',
    'UpdateTermPage',
    'UpdateWordPage',
)
