=======
Commits
=======

Type commits (required)
=======================

``feat``: – new functionality

``fix``: – bug fix

``docs``: – changes in documentation

``style``: – formatting, style edits (spaces, semicolons, etc.)

``refactor``: – refactoring code without changing behavior

``perf``: – performance related changes

``test``: – adding or correcting tests

``chore``: – minor changes (updating dependencies, CI settings, etc.)

Scoop (optional)
================

1. git

``docs(git)``: Adding, changing documentation on using git


Package/module scoop (optional)
===============================

1. app/

::

    wse/
    ├── app.py              # app
    ├── __main__.py         # app
    └── di_container.py     # app/di

2. config/

::

    config/
    ├── endpoints.yml       # config
    └── settings.py         # config

3. core/

::

    core/
    ├── api/                # api
    ├── auth/               # auth
    ├── navigation/         # navigation
    ├── storage/            # storage
    ├── i18n.py             # i18n
    └── di_container.py     # core/di



4. features/

::

    features/
    ├── base/               # base
    ├── shared/             # shared
    ├── main/               # main
    ├── foreign/            # foreign
    └── di_container.py     # features/di

5. interface/

::

    interface/
    ├── icore.py            # icore
    ├── ifeatures.py        # ifeatures
    └── imain.py            # ifeatures