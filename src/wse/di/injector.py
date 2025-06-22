"""Combine all injector modules to injector instance."""

from injector import Injector

from wse.config.di_module import ConfigModule
from wse.core.di_modules import CoreModule
from wse.features.apps.di_module import FeaturesAppsModule
from wse.features.apps.main import MAIN_APP_MODULES
from wse.features.apps.mathematics import MATH_APP_MODULES
from wse.features.shared.di_module import FeatureSharedModule


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
