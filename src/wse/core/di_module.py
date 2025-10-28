"""Defines Core injector module."""

from typing import no_type_check

import httpx
import toga
from injector import Binder, Module, provider, singleton

from wse.core.auth import AuthServiceProto
from wse.core.http.auth_schema import AuthSchema
from wse.core.http.client import HttpClient

from .api.auth_jwt import AuthAPIjwt
from .api.data import DataApi, DataApiABC
from .api.protocol import AuthAPIjwtProto
from .auth.service import AuthService
from .http import AuthSchemaProto, HttpClientProto
from .interfaces import Navigable
from .interfaces.istorage import JWTJsonStorageProto
from .navigation.navigator import Navigator
from .storage import JWTJsonStorage


class CoreModule(Module):
    """Core injector module."""

    @no_type_check
    def configure(self, binder: Binder) -> None:
        """Configure dependencies."""
        # Navigation service
        binder.bind(Navigable, to=Navigator, scope=singleton)

        # Storage service
        binder.bind(JWTJsonStorageProto, JWTJsonStorage)

        # Core API
        binder.bind(DataApiABC, to=DataApi)

        # Authentication service
        binder.bind(AuthServiceProto, to=AuthService, scope=singleton)
        binder.bind(AuthAPIjwtProto, to=AuthAPIjwt)

        # HTTP services
        binder.bind(HttpClientProto, to=HttpClient)
        binder.bind(AuthSchemaProto, to=AuthSchema, scope=singleton)

    @provider
    @singleton
    def provide_http_client(self) -> httpx.Client:
        """Provide the http client."""
        return httpx.Client()

    @provider
    @singleton
    def provide_main_window(self) -> toga.MainWindow:
        """Provide the Main window."""
        return toga.MainWindow()  # type: ignore[no-untyped-call]
