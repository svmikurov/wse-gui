"""Configure Main sub application features."""

from .di_module import MainRoutesModule
from .pages.home.di_module import HomeModule

# Initialize the injector bindings into `di.injector.create_injector()`
MAIN_APP_MODULES = [
    # Pages
    HomeModule(),
    # Page routes
    MainRoutesModule(),
]
