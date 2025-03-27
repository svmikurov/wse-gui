install:
	poetry install
	briefcase dev --no-run

test:
	briefcase dev --test

lint:
	ruff format --check
	ruff check

check: lint test

format:
	ruff format
	ruff check --fix

start:
	briefcase dev
