#!/bin/bash

# install requirements
pip install -r requirements.txt

# build and install python package
python setup.py clean --all
python setup.py build
python setup.py install

# build sphinx documentation (html and pdf with rinoh)
python -m sphinx -b html docs\source docs\build
python -m sphinx -b rinoh docs\source docs\build

# create executable for secure distribution
python -m PyInstaller installer.spec


