Development console errors
==========================

TypeErrors
----------

.. code-block:: console

   TypeError: Instance and class checks can only be used with @runtime_checkable protocols

Possible reason: Unbound dependency injected (error using library ``injector``)

Troubleshooting: Bound dependency with ``Module`` class of ``injector`` library

.. code-block:: python

   from typing import no_type_check
   from injector import Binder, Module

   class FooModule(Module):

       @no_type_check
       def configure(self, binder: Binder) -> None:
           ...
           binder.bind(BarInterface, to=Bar)
           +++++++++++++++++++++++++++++++++

Possible reason: Dependency not injected (error using library ``injector``)

Troubleshooting: Add ``@inject`` and ``@dataclass`` (optional) decorators,
add dependency annotation

.. code-block:: python

   from dataclasses import dataclass
   from injector import inject

   @inject
   @dataclass
   class Foo:

       bar: Bar

.. code-block:: python

   from injector import inject

   class Foo:

      @inject
      def __init__(self, bar: Bar): ...


injector.CallError
------------------

injector.CallError: Call to ABCMeta.__new__() failed: Can't instantiate abstract class WordParamsApiABC without an implementation for abstract method ...

Possible reason: Dependency inject into class constructor but not bound via ``injector.Module``

.. code-block:: python

   class WordParamsApi(WordParamsApiABC):

      @inject
      def __init__(
         self,
         http_client: httpx.Client,
         auth_scheme: AuthScheme,
         api_config: APIConfigV1,
      ) -> None:
         self._http_client = http_client
         self._auth_scheme = auth_scheme
         self._api_config = api_config

   def fetch_initial(self) -> WordParams:


   @inject
   @dataclass
   class WordStudyParamsNetworkRepo(WordStudyParamsNetworkRepoABC):

      _source: WordParamsNetworkSourceABC

      @override
      def fetch_initial(self) -> WordParams:
         return self._source.fetch_initial()

Troubleshooting: Bound ``WordParamsApiABC`` with ``WordParamsApi```

.. code-block:: python

   from injector import Binder, Module
   ...

   class ApiModule(Module):
      """API requests DI module."""

      @no_type_check
      @override
      def configure(self, binder: Binder) -> None:
         """Configure dependencies."""
         ...
         binder.bind(WordParamsApiABC, to=WordParamsApi)
         ...