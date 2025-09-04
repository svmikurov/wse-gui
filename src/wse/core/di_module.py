"""Defines Core injector module."""

from typing import no_type_check

import httpx
import toga
from injector import Binder, Module, provider, singleton

from wse.apps.main.api import AssignedApiProto
from wse.apps.main.api.assigned import AssignedApiClient
from wse.apps.math.api.calculation import CalculationApiClient
from wse.apps.math.api.protocol import CalculationApiProto
from wse.core.auth import AuthServiceProto
from wse.core.http.auth_schema import AuthSchema
from wse.core.http.client import HttpClient

from .api import AuthAPIjwtProto
from .api.auth_jwt import AuthAPIjwt
from .auth.service import AuthService
from .http import AuthSchemeProto, HttpClientProto
from .interfaces import NavigatorProto
from .interfaces.istorage import JWTJsonStorageProto
from .navigation.navigator import Navigator
from .storage import JWTJsonStorage


class CoreModule(Module):
    """Core injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        # Navigation service
        binder.bind(NavigatorProto, to=Navigator, scope=singleton)

        # Storage service
        binder.bind(JWTJsonStorageProto, JWTJsonStorage)

        # Authentication service
        binder.bind(AuthServiceProto, to=AuthService, scope=singleton)
        binder.bind(AuthAPIjwtProto, to=AuthAPIjwt)

        # HTTP services
        binder.bind(HttpClientProto, to=HttpClient)
        binder.bind(AuthSchemeProto, to=AuthSchema, scope=singleton)

        # Exercise API services
        binder.bind(AssignedApiProto, to=AssignedApiClient)
        binder.bind(CalculationApiProto, to=CalculationApiClient)

    @provider
    @singleton
    def provide_http_client(self) -> httpx.Client:
        """Provide the http client."""
        return httpx.Client()

    @provider
    @singleton
    def provide_main_window(self) -> toga.MainWindow:
        """Provide the Main window."""
        return toga.MainWindow()
