import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Beamon",
    version="0.1",
    author="Maher Albezem",
    author_email="maher.ablezem@sla.rwth-aachen.de",
    description=("Simulationstool für Tragwerksstrukturen"),
    license = "QPL",
    keywords = "Tragwerke SQLite3",
    url = "https://git.rwth-aachen.de/maher.albezem/beamon",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Environment :: X11 Applications :: Qt",
        "Environment :: Console",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Natural Language :: German",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: Free For Educational Use",
    ],
)