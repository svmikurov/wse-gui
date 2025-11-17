"""Foreign discipline Presentation params container tests."""

import pytest
from injector import Injector

from wse.feature.di_module import FeatureModule
from wse.ui.containers.di_module import UIContainerModule
from wse.ui.containers.params.container import ParamsContainer
from wse.ui.di_module import UIModule


@pytest.fixture
def container() -> ParamsContainer:
    """Provide dependency injector."""
    injector = Injector(
        [
            FeatureModule(),
            UIModule(),
            UIContainerModule(),
        ]
    )
    return injector.get(ParamsContainer)


class TestInstantiating:
    """Presentation params container instantiating tests."""

    def test_container_instantiating(
        self,
        container: ParamsContainer,
    ) -> None:
        """Test the container instantiating."""
        assert container
