include .env	# import TEST_JUST var

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

check: ruff test

# Briefcase for android
android:
	briefcase run android

android-create:
	briefcase create android

android-build:
	briefcase build android

android-update: android-create android-build android

gettext:
	msgfmt -o src/wse/locales/ru/LC_MESSAGES/app.mo src/wse/locales/ru/LC_MESSAGES/app.po && \
	msgfmt -o src/wse/locales/en/LC_MESSAGES/app.mo src/wse/locales/en/LC_MESSAGES/app.po
