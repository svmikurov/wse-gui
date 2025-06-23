"""Combine all injector modules to injector instance."""

from injector import Injector

from wse.config.di_module import ConfigModule
from wse.core.di_modules import CoreModule
from wse.features.shared.di_module import FeatureSharedModule
from wse.features.subapps.di_module import FeaturesAppsModule
from wse.features.subapps.main import MAIN_APP_MODULES
from wse.features.subapps.mathematics import MATH_APP_MODULES


def create_injector() -> Injector:
    """Combine all injector modules to injector instance."""
    return Injector(
        [
            ConfigModule(),
            CoreModule(),
            FeaturesAppsModule(),
            FeatureSharedModule(),
        ]
        + MAIN_APP_MODULES
        + MATH_APP_MODULES
    )
