WSE GUI
=======

# Install development mode

## Create environment
```commandline
python3.11 -m venv .venv_wsegui
source .venv_wsegui/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

## Fix errors
```commandline
sudo apt update
sudo apt install -y python3.11-dev pkg-config
```

## Localise project
```commandline
make gettext
```