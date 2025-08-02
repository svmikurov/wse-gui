"""Configure Mathematics sub application features."""

from .di_module import MathAppModule
from .pages.index.di_module import IndexMathModule
from .pages.simple_calc.di_module import SimpleCalculationModule
from .sources.di_module import MathSourcesModule

# Initialize the injector bindings into `di.injector.create_injector()`
MATH_APP_MODULES = [
    # Pages
    IndexMathModule(),
    SimpleCalculationModule(),
    # Sources
    MathSourcesModule(),
    # Page routes
    MathAppModule(),
]
