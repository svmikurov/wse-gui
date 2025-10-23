Add style and theme
===================

.. seealso:: `Toga style <https://toga.readthedocs.io/en/stable/reference/style/pack.html>`_

Let's add style and theme to ``BarContainer``.

There are stages to adding style/theme:

- :ref:`update-json`
- :ref:`define-dto`
- add to ``injector.Module`` method to:

  * load JSON
  * initialize DTO
  * provide DTO

- inject DTO into view/container
- assign style/theme to widget

.. _update-json:

Update JSON
-----------

All configuration files are live by path: ``wse/resources/style/``.

Add ``bar_container`` style configuration to other.

.. code-block:: json
   :caption: wse/resources/style/style_default.json:
   :emphasize-lines: 9-26

   {
       "window_size": [440, 700],
       "label_title": {
           "font_size": 20,
           "text_align": "center",
           "margin_top": 15,
           "margin_bottom": 15
       },
       "bar_container": {
           "label_title": {
               "font_size": 15,
               "height": 60,
               "margin_top": 2,
               "margin_right": 5,
               "margin_bottom": 2,
               "margin_left": 5
           },
           "button": {
               "font_size": 15,
               "height": 60,
               "margin_top": 2,
               "margin_right": 5,
               "margin_bottom": 2,
               "margin_left": 5
           }
       }
   }

We've added style to the ``label title`` and ``button`` widgets
defined as attributes of the ``BarContainer`` class.

The structure of the theme's JSON configuration for these same widgets
is defined in a similar way.

.. code-block:: json
   :caption: wse/resources/style/theme_default.json:
   :emphasize-lines: 5-13

   {
       "label_title": {
          "color": "red"
       },
       "bar_container": {
           "label_title": {
               "color": "blue"
           },
           "button": {
               "color": "yellow",
               "background_color": "green"
          }
       }
   }

.. _define-dto:

Define DTO
----------
