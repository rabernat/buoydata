import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "buoydata",
    version = "0.0.1",
    author = "Ryan Abernathey",
    author_email = "rpa@ldeo.columbia.edu",
    description = ("Tools for reading NOAA Global Drifter Program data."),
    license = "MIT",
    keywords = "science oceanography",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=['buoydata'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
)
