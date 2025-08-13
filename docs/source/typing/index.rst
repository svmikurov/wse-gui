Type checking
=============

Using `@no_type_check`
----------------------

When binding a method by interface using the injector library method,
a "[type-abstract]" error occurs when checking with mypy.

.. code-block:: python

   from typing import no_type_check
   from injector import Binder, Module

   class HomePageModule(Module):
       """Home page module container."""

       @no_type_check
       def configure(self, binder: Binder) -> None:
           """Configure the bindings."""
           binder.bind(IHomeView, to=HomeView)
           binder.bind(IHomeController, to=HomeController)

.. code-block:: bash
   :caption: Errors that occurs when decorator is missing:

   error: Only concrete class can be given where "type[IHomeView]" is expected  [type-abstract]
   error: Only concrete class can be given where "type[IHomeController]" is expected  [type-abstract]
