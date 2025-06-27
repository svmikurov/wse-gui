"""Combine all injector modules to injector instance."""

from injector import Injector

from wse.config.di_module import ConfigModule
from wse.core.di_modules import CoreModule
from wse.features.services.di_module import FeatureServicesModule
from wse.features.shared.components.di_module import ComponentsModule
from wse.features.shared.containers.di_module import SharedContainersModule
from wse.features.shared.di_module import FeatureSharedModule
from wse.features.shared.widgets.di_module import WidgetsModule
from wse.features.subapps.di_module import FeaturesAppsModule
from wse.features.subapps.main.apps import MAIN_APP_MODULES
from wse.features.subapps.math.apps import MATH_APP_MODULES


def create_injector() -> Injector:
    """Combine all injector modules to injector instance."""
    return Injector(
        [
            ConfigModule(),
            CoreModule(),
            FeaturesAppsModule(),
            FeatureServicesModule(),
            FeatureSharedModule(),
            SharedContainersModule(),
            WidgetsModule(),
            ComponentsModule(),
        ]
        + MAIN_APP_MODULES
        + MATH_APP_MODULES
    )
