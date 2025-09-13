"""Abstract base classes for Assigned exercise UI layer."""

from abc import ABC
from typing import Literal

from wse.data.sources.user import UserObserverABC
from wse.feature.base import ViewABC
from wse.feature.base.mixins import AddObserverGenT

# State

_StateNotifyT = Literal['']


class AssignedStateFeatureABC(ABC):
    """ABC for Assigned exercise UI state feature."""

    ...


class AssignedStateObserverABC(ABC):
    """ABC for Assigned exercise UI state observer."""

    ...


class AssignedViewModelABC(
    AssignedStateFeatureABC,
    AddObserverGenT[AssignedStateObserverABC, _StateNotifyT],
    UserObserverABC,
    ABC,
):
    """ABC for Assigned exercise ViewModel."""


# View


class AssignedViewABC(
    AssignedStateObserverABC,
    ViewABC,
    ABC,
):
    """ABC for Assigned exercise View."""
