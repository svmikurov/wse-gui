Simple page dependency injection
================================

To inject our page view and controller as dependency define ``HomeModule`` class
and add it to ``MAIN_APP_MODULES`` list into ``apps.main.apps`` module.

.. code-block:: python
   :caption: src/wse/apps/main/pages/home/di_module.py:

   from injector import Binder, Module

   from .interfaces import IHomeController, IHomeView
   from .controller import HomeController
   from .model import HomeModel

   class HomeModule(Module):

       @no_type_check
       def configure(self, binder):
           binder.bind(IHomeModel, to=HomeModel)
           binder.bind(IHomeView, to=HomeView)


.. code-block:: python
   :caption: src/wse/apps/main/apps.py:

   MAIN_APP_MODULES = [
       HomeModule(),
       ...
    ]
