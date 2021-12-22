# PythonifyCpp
A working example of exposing C++(11) functions to Python using Boost-Python.

## Installation and Usage

Once Python3 is installed, we can use Boost-Python to expose C++ functions to Python. Apart from the direct installation, [Boost](https://www.boost.org/) can be more conveniently installed via command line using [(Mini)conda](https://docs.conda.io/en/latest/miniconda.html) by doing

```
conda install -c conda-forge boost
```

or using homebrew (only for **nix* systems) by doing

```
brew install boost
```



Once Boost is installed in the system and is in Python's path, the Boost-Python library should be included in the __*setup.py*__ file (as done for example in the default __*setup.py*__ file that comes with this repository where `libraries=['boost_python38']` for python3.8, for example.).



And, to build, run the following command

```
python setup.py --quiet build_ext --inplace clean --all
```



Finally a file of the form __*PowerPy.xxxx.so*__ should appear in the *src* directory which can be readily imported into Python. Since __*\_\_init\_\_.py*__ has the docstrings for each of the C++ function, they can be accessed by simply importing the __*src*__ directory, as a whole, as a python package. For purposes of illustration, this package just has two simple functions, one to find a square and the other to find cube of a number. More complicated functions can be declared in a header file and then included in the *.cc* file before the build. At Python prompt, do

```python
import src as PowerPy
PowerPy.square(2)#To find square of 2
PowerPy.cube(2)#To find cube of 2
```

to start using the C++ code as a Python package!

(The repository at https://github.com/flipdazed/boost-python-hello-world was useful in creating this repository.)
