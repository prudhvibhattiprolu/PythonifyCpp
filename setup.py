#To build:
# >>> python setup.py --quiet build_ext --inplace clean --all

import os
import sys
from glob import glob
import setuptools
from setuptools import setup

#Use pybind11 to expose C++ functions to Python
DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR, "pybind11"))

from pybind11.setup_helpers import Pybind11Extension, build_ext

del sys.path[-1]

with open("README.md", "r") as README:
    long_description = README.read()

#Provide information about the external C++ wrapper file that exposes C++
#functions to Python
PowerPy = Pybind11Extension(
    'PowerPy',#name of the package
    sources=['PowerPy.cc'],#path to the C++ wrapper file
    language = 'c++',
    #Include path to libraries using "-I <path to libraries>" below
    extra_compile_args = ['-std=c++11', '-I .']
)

#Package info
setup(
    name="PowerPy",
    version="2.0",
    author="Prudhvi Bhattiprolu",
    author_email="prudhvibhattiprolu@gmail.com",
    description="A minimal self-contained working example of exposing C++(11) functions to Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    ##If you want to use src directory structure, move the source code to src
    ##and uncomment below two lines
    #packages=setuptools.find_packages(where="src"),
    #package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    cmdclass={"build_ext": build_ext},
    ext_modules=[PowerPy]
)
