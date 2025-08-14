"""Defines Assigned exercise page injector module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import AssignedController
from .iabc import IAssignedController, IAssignedModel, IAssignedView
from .model import AssignedModel
from .view import AssignedView


class AssignedModule(Module):
    """Login page injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(IAssignedModel, to=AssignedModel)
        binder.bind(IAssignedView, to=AssignedView)
        binder.bind(IAssignedController, to=AssignedController)
