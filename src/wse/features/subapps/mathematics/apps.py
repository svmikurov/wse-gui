"""Configure Mathematics sub application features."""

from .di_module import MathRoutesModule
from .pages.index.di_module import IndexMathPageModule
from .pages.simple_calculation.di_module import SimpleCalculationPageModule

# Initialize the injector bindings into `di.injector.create_injector()`
MATH_APP_MODULES = [
    # Pages
    IndexMathPageModule(),
    SimpleCalculationPageModule(),
    # Page routes
    MathRoutesModule(),
]
