#To build:
# >>> python setup.py --quiet build_ext --inplace clean --all


import setuptools
from distutils.core import setup
from distutils.extension import Extension

with open("README.md", "r") as README:
    long_description = README.read()

PowerPy = Extension(
    'PowerPy',
    sources=['src/PowerPy.cc'],
    #library_dirs=['in case of issues regarding boost-python library, path to the directory containing that library goes here'],
    libraries=['boost_python38'],
)

setup(
    name='PowerPy',
    version='1.0',
    author="Prudhvi Bhattiprolu",
    author_email="prudhvibhattiprolu@gmail.com",
    description="A working example of exposing C++(11) functions to Python using Boost-Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    ext_modules=[PowerPy]
    )
