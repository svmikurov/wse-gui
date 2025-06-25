"""Configure Mathematics sub application features."""

from .di_module import MathRoutesModule
from .pages.index.di_module import IndexMathModule
from .pages.simple_calculation.di_module import SimpleCalculationModule

# Initialize the injector bindings into `di.injector.create_injector()`
MATH_APP_MODULES = [
    # Pages
    IndexMathModule(),
    SimpleCalculationModule(),
    # Page routes
    MathRoutesModule(),
]
