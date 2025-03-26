install:
	poetry install
	briefcase dev --no-run

test:
	briefcase dev --test

lint:
	ruff format --check
	ruff check

check: test lint

format:
	ruff format
	ruff check --fix
