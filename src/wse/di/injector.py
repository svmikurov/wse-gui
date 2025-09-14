"""Combine all injector modules to injector instance."""

from injector import Injector

from wse.config.di_module import ConfigModule
from wse.core.di_module import CoreModule
from wse.data.repositories.di_module import RepoModule
from wse.data.sources.di_module import SourceModule
from wse.domain.di_module import UseCaseModule
from wse.feature.api.di_module import ApiModule
from wse.feature.services.di_module import FeatureServicesModule
from wse.feature.shared.containers.di_module import ContainerModule
from wse.feature.shared.di_module import FeatureSharedModule
from wse.feature.shared.widgets.di_module import WidgetsModule
from wse.feature.source_wraps.di_module import SourceWrapsModule
from wse.ui.di_module import UIModule
from wse.ui.main.di_module import HomeModule
from wse.ui.math.di_module import MathUIModule


def create_injector() -> Injector:
    """Combine all injector modules to injector instance."""
    return Injector(
        [
            # config/
            ConfigModule(),
            # core/
            CoreModule(),
            # features/
            ApiModule(),
            FeatureServicesModule(),
            FeatureSharedModule(),
            WidgetsModule(),
            ContainerModule(),
            # ui/
            UIModule(),
            HomeModule(),
            MathUIModule(),
            # domain/
            UseCaseModule(),
            # data/
            RepoModule(),
            SourceModule(),
            SourceWrapsModule(),
            # TODO: Refactor
        ]
    )
