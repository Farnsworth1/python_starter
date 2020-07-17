Repo Structure
***************

For structuring python projects read the Hitchhiker's Guid to Python `here
<https://docs.python-guide.org/writing/structure/>`_.

Repository overall structure
============================
>>> tree /F
.
│   .gitignore
│   installer.spec
│   LICENSE
│   README.md
│   requirements.txt
│   runme.sh
│   setup.py
│
├───.idea
├───beamon
│   │   core.py
│   │   runapp.py
│   │   __init__.py
│   │
│   └───__pycache__
│           core.cpython-37.pyc
│           runapp.cpython-37.pyc
│           __init__.cpython-37.pyc
│
├───Beamon.egg-info
├───build
├───dist
│       Beamon-0.1-py3.7.egg
│       runbeamon.exe
│
├───docs
│   ├───build
│   └───source
├───resources
│   │   innosetup-6.0.5.exe
│   │   Winpython64-3.8.3.0.exe
│   │
│   └───UML
│
└───tests


Discription
===========

The Actual Modul:
This is where the core focus of the repository is.

+------------+------------------------+
| Location   |  ./beamon/             |
+------------+------------------------+
| Purpose    | Programms code         |
+------------+------------------------+

License:

+------------+------------------------+
| Location   |  ./LICENSE             |
+------------+------------------------+
| Purpose    | Copyright              |
+------------+------------------------+

Setup.py:

+------------+-------------------------------------+
| Location   |  ./setup.py                         |
+------------+-------------------------------------+
| Purpose    | Package and distribution management.|
+------------+-------------------------------------+

PyInstaller Specification:

+------------+-------------------------------------+
| Location   |  ./installer.spec                   |
+------------+-------------------------------------+
| Purpose    | secure distribution management.     |
+------------+-------------------------------------+

Distribution files:

+------------+--------------------------------------+
| Location   |  ./dist/                             |
+------------+--------------------------------------+
| Purpose    | distributing Beamon as package or exe|
+------------+--------------------------------------+

Requirements File:

+------------+-------------------------+
| Location   |  ./requirements.txt     |
+------------+-------------------------+
| Purpose    | Development dependencies|
+------------+-------------------------+

Documentation:

+------------+---------------------------------+
| Location   |  ./docs/                        |
+------------+---------------------------------+
| Purpose    | Package reference documentation.|
+------------+---------------------------------+

Test Suite:

+------------+------------------------------------+
| Location   |  ./tests/                          |
+------------+------------------------------------+
| Purpose    | Package integration and unit tests.|
+------------+------------------------------------+


