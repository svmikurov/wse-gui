"""Main feature package."""

from .di_module import MainRoutesModule
from .pages.home.di_module import HomePageModule

MAIN_APP_MODULES = [
    # Pages
    HomePageModule(),
    # Page routes
    MainRoutesModule(),
]
