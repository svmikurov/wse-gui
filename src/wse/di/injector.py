"""Combine all injector modules to injector instance."""

from injector import Injector

from wse.apps.di_module import FeaturesAppsModule
from wse.apps.main.apps import MAIN_APP_MODULES
from wse.apps.math.apps import MATH_APP_MODULES
from wse.config.di_module import ConfigModule
from wse.core.di_module import CoreModule
from wse.data.di_module import DataModule
from wse.data.repositories.di_module import RepositoryModule
from wse.data.sources.di_module import SourceModule
from wse.domain.di_module import UseCaseModule
from wse.feature.services.di_module import FeatureServicesModule
from wse.feature.shared.containers.di_module import ContainerModule
from wse.feature.shared.di_module import FeatureSharedModule
from wse.feature.shared.widgets.di_module import WidgetsModule
from wse.ui.di_module import UIModule


def create_injector() -> Injector:
    """Combine all injector modules to injector instance."""
    return Injector(
        [
            # config/
            ConfigModule(),
            # core/
            CoreModule(),
            # features/
            FeaturesAppsModule(),
            FeatureServicesModule(),
            FeatureSharedModule(),
            WidgetsModule(),
            ContainerModule(),
            # ui/
            UIModule(),
            # domain/
            UseCaseModule(),
            # data/
            RepositoryModule(),
            SourceModule(),
            # Temporary for architecture study
            DataModule(),
        ]
        # features/subapps/
        + MAIN_APP_MODULES
        + MATH_APP_MODULES
    )
