"""Configure Main sub application features."""

from .di_module import MainRoutesModule
from .pages.assigned.di_module import AssignedModule
from .pages.auth.di_module import LoginModule
from .pages.exercise.di_module import ExerciseModule
from .pages.home.di_module import HomeModule

# Initialize the injector bindings into `di.injector.create_injector()`
MAIN_APP_MODULES = [
    # Pages
    HomeModule(),
    LoginModule(),
    AssignedModule(),
    ExerciseModule(),
    # Page routes
    MainRoutesModule(),
]
