"""Defines Assigned exercise page injector module."""

from typing import no_type_check

from injector import Binder, Module

from .controller import AssignationsController
from .model import AssignationsModel
from .protocols import (
    AssignationsControllerProto,
    AssignationsModelProto,
    AssignationsViewProto,
)
from .view import AssignationsView


class AssignedModule(Module):
    """Login page injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure the bindings."""
        binder.bind(AssignationsModelProto, to=AssignationsModel)
        binder.bind(AssignationsViewProto, to=AssignationsView)
        binder.bind(AssignationsControllerProto, to=AssignationsController)
