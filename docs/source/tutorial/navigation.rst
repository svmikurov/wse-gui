Simple page navigation
======================

Each page has its own ID for navigation.

Let's define a navigation ID for our page using the :class:`~wse.apps.nav_id.NavID` enumeration.

.. code-block:: python
   :caption: src/wse/apps/nav_id.py:
   :emphasize-lines: 3

    class NavID(BaseEnum):

        HOME = 'Home page'
        ...

The project :ref:`consists of applications <Project architecture>`.
We created page in `main` app.
So in the `apps.main.routes` module we will bind the ``IHomeController`` of our page to the ``NavID.HOME``.

.. code-block:: python
   :caption: src/wse/apps/main/apps.py:
   :emphasize-lines: 7

   class MainRoutes(BaseRoutes):

       @property
       @no_type_check
       def routes(self):
            return {
                NavID.HOME: self._injector.get(IHomeController),
                ...
            }
