"""Configure Main sub application features."""

from .di_module import MainRoutesModule
from .pages.assigned.di_module import ExerciseModule

# Initialize the injector bindings into `di.injector.create_injector()`
MAIN_APP_MODULES = [
    # Pages
    ExerciseModule(),
    # Page routes
    MainRoutesModule(),
]
