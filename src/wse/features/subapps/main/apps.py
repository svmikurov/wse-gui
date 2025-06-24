"""Configure Main sub application features."""

from .di_module import MainRoutesModule
from .pages.home.di_module import HomePageModule

# Initialize the injector bindings into `di.injector.create_injector()`
MAIN_APP_MODULES = [
    # Pages
    HomePageModule(),
    # Page routes
    MainRoutesModule(),
]
