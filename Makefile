# Include
include .env  # TEST_JUST var

# Radon code analysis
RADON_SOURCES = src/
RADON_EXCLUDE = "tests/*,venv/*,.venv/*"

# Colors
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED = \033[0;31m
NC = \033[0m  # No Color

install:
	poetry install
	briefcase dev --no-run

start:
	briefcase dev

# Test
test:
	export TOGA_BACKEND=toga_dummy && \
	pytest

test-just:
	export TOGA_BACKEND=toga_dummy && \
	pytest $(TEST_JUST) -sv

test-briefcase:
	export TOGA_BACKEND=toga_dummy && \
	briefcase dev --test

test-r:
	export TOGA_BACKEND=toga_dummy && \
	briefcase dev --test -r

ruff:
	ruff check && ruff format --diff

format:
	ruff check --fix && ruff format

check: format ruff test

# Briefcase for android
android:
	briefcase run android

android-create:
	briefcase create android

android-build:
	briefcase build android

android-update: android-create android-build android

# Radon code analysis
.PHONY: radon-check
radon-check:
	@echo "${YELLOW}=== Cyclomatic Complexity ===${NC}"
	@radon cc --min B --exclude $(RADON_EXCLUDE) $(RADON_SOURCES)
	@echo "${YELLOW}=== Maintainability Index ===${NC}"
	@radon mi --min B --exclude $(RADON_EXCLUDE) $(RADON_SOURCES)