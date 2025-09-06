WSE GUI
=======

### Note: Development of this version has been discontinued due to changes in the application architecture.



# Install development mode

## Create environment
```commandline
python3.11 -m venv .venv_wsegui
source .venv_wsegui/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

## Fix install errors
```commandline
sudo apt update
sudo apt install -y python3.11-dev pkg-config
```

## Localize the project
```commandline
make localize
```