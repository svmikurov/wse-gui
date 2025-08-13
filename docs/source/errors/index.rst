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
