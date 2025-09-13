"""Configure Main sub application features."""

from .di_module import MainRoutesModule
from .pages.assignations.di_module import AssignedModule
from .pages.assigned.di_module import ExerciseModule

# Initialize the injector bindings into `di.injector.create_injector()`
MAIN_APP_MODULES = [
    # Pages
    AssignedModule(),
    ExerciseModule(),
    # Page routes
    MainRoutesModule(),
]
