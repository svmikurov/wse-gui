"""Mathematics application feature."""

from .di_module import MathRoutesModule
from .pages.index.di_module import IndexMathPageModule

MATH_APP_MODULES = [
    # Pages
    IndexMathPageModule(),
    # Page routes
    MathRoutesModule(),
]
