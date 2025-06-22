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
check: format mypy

# Update and build android `app-debug.apk` fail
# to create `.apk` fail: briefcase create android
update-android:
	briefcase update android
	briefcase build android