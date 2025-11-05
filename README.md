WSE GUI
=======

__NOTE: The application architecture is being refactored 
like [Android app](https://developer.android.com/topic/architecture?hl=ru#recommended-app-arch)__

# Install development mode

## Create environment
```commandline
python3 -m venv .venv_wsegui
source .venv_wsegui/bin/activate
```

## Platform-specific dependencies
For Debian 13+ (for other platform [see](https://toga.readthedocs.io/en/stable/tutorial/tutorial-0.html) )
```commandline
sudo apt update
sudo apt install git build-essential pkg-config python3-dev libgirepository-2.0-dev libcairo2-dev gir1.2-gtk-3.0 libcanberra-gtk3-module
```

Install gettext package
```commandline
sudo apt-get update && sudo apt-get install gettext
```

## Install development dependency
```commandline
pip install -r requirements-dev.txt
```


## Localize the project
```commandline
make localize
```

## Run tests
```commandline
make test
```

## Run development mode
```commandline
make start
```

### Combined commands
Combined commands to install python dependencies
```commandline
git clone git@github.com:svmikurov/wse-gui.git
cd wse-gui/
python3 -m venv .venv_wsegui
source .venv_wsegui/bin/activate
pip install -r requirements-dev.txt
make localize
make test
make start
```