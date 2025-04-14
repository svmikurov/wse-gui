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

The scoop can be used in combination (scoop/under scoop).

For example:

``(app/di)`` - Make changes to the ``di`` scoop of the ``app`` scoop

``(core/di)`` - Make changes to the ``di`` scoop of the ``core`` scoop

``(features/di)`` - Make changes to the ``di`` scoop of the ``features`` scoop
                    affecting all under scoop (``features/main``, ``features/foreign``, ...)

``(main/di)`` - Make changes to the ``di`` scoop of the ``features/main`` scoop

Feature scoop (optional)
========================

1. git

For example:

``docs(git)``: Adding, changing documentation on using git

``chore(git)``: Add token.enc to ignored files


Package/module scoop (optional)
===============================

1. app/

::

    wse/                    # Scoop:
    ├── app.py              # (app)
    ├── __main__.py         # (app)
    └── di_container.py     # (app/di)

2. config/

::

    config/                 # Scoop:
    ├── endpoints.yml       # (config)
    └── settings.py         # (config)

3. core/

::

    core/                   # Scoop:
    ├── api/                # (api)
    |   └── auth.py         # (api/auth)
    ├── auth/               # (auth)
    ├── navigation/         # (navigation)
    ├── storage/            # (storage)
    ├── i18n.py             # (i18n)
    └── di_container.py     # (core/di), (navigation/di)



4. features/

::

    features/               # Scoop:
    ├── base/               # (base)
    ├── shared/             # (shared)
    ├── main/               # (main), (main/auth)
    ├── foreign/            # (foreign)
    └── di_container.py     # (features/di)

5. interface/

::

    interface/              # Scoop:
    ├── icore.py            # (icore)
    ├── ifeatures.py        # (ifeatures)
    └── imain.py            # (ifeatures/main)