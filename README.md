# Python Starter
Some discription of the Project:
Beamon is a database-based program for modeling static structures. 
The simulation of such Structures are made with CALFEM-Python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements from requirements.txt file.

run bash file ``runme.sh``

## Usage
### How to use beamon package
You can import package beamon in your Python script using the following code:
```python
import beamon

beamon.run("test.txt")
```

## Contributing
This section could be placed in CONTRIBUTING.md file.

### How to install required python Packages
Running the command `pip install -r requirements.txt` inside the root project directory you will be able to install
all required packages inside the python environment of your choice (I personally recommend Anaconda environments)  

### How To Build Sphinx Documentation

- build html documentation using `make html` command inside `docs` directory
- build PDF documentation using `sphinx-build -b rinoh . _build/rinoh` command inside `docs` directory


Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Last but not least the most important part of your project.
