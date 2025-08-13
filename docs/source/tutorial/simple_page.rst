Create simple page
==================

The application uses the MVC model.
Let's layout a simple page example without a model.

Create ``HomePage``:

- create ``HomeView``
- create ``HomeController``

``HomeView`` contains UI elements.

``HomeController`` creates an instance of ``HomeView`` and provide it content to ``main_window`` for display.

Create simple view
------------------

For a simple example, we'll add only a page title widget.

Let's inherit our view from the ``BaseView`` and override the its methods:

- ``_create_ui()``
- ``_populate_content()``
- ``localize_ui()``

These methods will be called when the view is initialized.

To crate widget use ``_create_ui()`` abstract base method.

.. code-block:: python
   :caption: src/wse/apps/main/pages/home/view.py:

   class HomeView(BaseView):

       def _create_ui(self):
           self._label_title = toga.Label('')

We will add text for widget later.

Now add a title to the page content.

All page widgets are stored in the ``_content`` class attribute.

To add a widget to a page use the ``_populate_content()`` method.

.. code-block:: python

       ...

       def _populate_content(self):
           self._content.add(self._label_title)

Now let's add the title text.

The application supports international translations.
A ``label_()`` function of the ``utils.i18n`` module is used to translate titles.
See the ``utils.i18n`` module for other translation functions.

To assign text to a widget, use the ``localize_ui()`` method.

If there is a need to change the application language without restarting it,
the ``localize_ui()`` method will be called and apply the translation to all widgets.

.. code-block:: python

       ...

       def localize_ui(self):
           self._label_title.text = label_('Home page')

We looked at a simple example of adding a widget to a page.

Create simple controller
------------------------

Inherit page controller from ``BasePageController``.
   :caption: src/wse/apps/main/pages/home/controller.py:

.. code-block:: python

   class HomeController(BasePageController):

       _view: IHomeView

To bind the controller to the view, we annotated the page view in the page controller class with `IHomeView` protocol.

.. code-block:: python
   :caption: src/wse/apps/main/pages/home/interfaces.py:

   class IHomeView(IView, Protocol):
      ...

   class IHomeController(IPageController, Protocol):
      ...

To display a page, the controller initializes the view and provides page ``content`` with view widgets.

.. code-block:: python
   :caption: BasePageController.content

    @property
    def content(self):
        return self._view.content

Inject dependencies for simple page
-----------------------------------

The application uses the ``injector`` library to inject dependencies

Let's mark our class with decorators so that dependencies are injected and take a look at our code.

.. code-block:: python
   :caption: For example, the modules are combined:

   from dataclasses import dataclass
   from injector import inject

   from wse.features.base.mvc import BasePageController
   from wse.features.base import BaseView
   from wse.utils.i18n import label_

   @inject
   @dataclass
   class HomeView(BaseView):

       def _create_ui(self):
           self._label_title = toga.Label('')

       def _populate_content(self):
           self._content.add(self._label_title)

       def localize_ui(self):
           self._label_title.text = label_('Home page')

   @inject
   @dataclass
   class HomeController(BasePageController):

       _view: HomeView

Conclusion on create simple page
--------------------------------

We created a simple page.

We overridden the base view class methods to add the page title.

We bound page view with page controller.

We used the ``injector`` library together with the ``dataclass`` to inject page dependency.

To display the page we need to:

- add the page to the navigation system
- set up dependency injection

But that's beyond the scope of creating a page.

Next:

- Adding pages to navigation
- Configure the dependency injection
- Adding widget styles
- Creating a page model
- Using services