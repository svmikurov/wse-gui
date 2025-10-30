# Run the application in development mode
start:
	briefcase dev

# Code style checking
ruff:
	ruff check && ruff format --diff

format:
	ruff check --fix && ruff format

# Static type checking
mypy:
	mypy --strict .

# Code checking
check: format mypy test

# Test
test:
	briefcase dev --test

# Update and build android `app-debug.apk` fail.
# To create `.apk` file enter: briefcase create android
update-android:
	briefcase update android
	briefcase build android

# Localization
DOMAINS = nav label core exercise
LANGUAGES = en ru
LOCALE_DIR = src/wse/resources/locale
MO_FILES = $(foreach lang,$(LANGUAGES), \
            $(foreach domain,$(DOMAINS), \
                $(LOCALE_DIR)/$(lang)/LC_MESSAGES/$(domain).mo))
localize: $(MO_FILES)
$(LOCALE_DIR)/%.mo: $(LOCALE_DIR)/%.po
	msgfmt -o $@ $<