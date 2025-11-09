"""Combine all injector modules to injector instance."""

from injector import Injector

from wse.api.di_module import ApiModule
from wse.config.di_module import ConfigModule
from wse.core.di_module import CoreModule
from wse.data.repos.di_module import RepoModule
from wse.data.sources.di_module import SourceModule
from wse.domain.di_module import UseCaseModule
from wse.feature.di_module import FeatureModule
from wse.feature.services.di_module import FeatureServicesModule
from wse.feature.source.wraps.di_module import SourceWrapsModule
from wse.ui.containers.di_module import UIContainerModule
from wse.ui.di_module import UIModule
from wse.ui.foreign.di_module import ForeignModule
from wse.ui.glossary.di_module import GlossaryModule
from wse.ui.main.di_module import HomeModule
from wse.ui.math.di_module import MathUIModule
from wse.ui.widgets.di_module import WidgetsModule


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
            FeatureModule(),
            WidgetsModule(),
            # ui/
            UIModule(),
            UIContainerModule(),
            HomeModule(),
            MathUIModule(),
            GlossaryModule(),
            ForeignModule(),
            # domain/
            UseCaseModule(),
            # data/
            RepoModule(),
            SourceModule(),
            SourceWrapsModule(),
        ]
    )
