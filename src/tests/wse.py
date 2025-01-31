"""Test settings."""

import os
import sys
import tempfile
from pathlib import Path

import pytest


def run_tests() -> None:
    """Run tests."""
    project_path = Path(__file__).parent.parent.parent
    os.chdir(project_path)

    # Determine any args to pass to pytest. If there aren't any,
    # default to running the whole test suite.
    args = sys.argv[1:]
    if len(args) == 0:
        args = [
            'src',
            # 'src/tests/page/test_params_widget.py',
        ]

    returncode = pytest.main(
        [
            # Include doctests
            '--doctest-modules',
            '-s',
            # Turn up verbosity
            '-vv',
            # Disable color
            '--color=yes',
            # Overwrite the cache directory to somewhere writable
            '-o',
            f'cache_dir={tempfile.gettempdir()}/.pytest_cache',
        ]
        + args
    )

    print(f'>>>>>>>>>> EXIT {returncode} <<<<<<<<<<')


if __name__ == '__main__':
    run_tests()
