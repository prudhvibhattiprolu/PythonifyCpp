# PythonifyCpp
A minimal self-contained working example of exposing C++(11) functions to Python using a light-weight header-only [pybind11](https://pybind11.readthedocs.io/en/stable/) library.

## File dependencies

* [pybind11](https://pybind11.readthedocs.io/en/stable/) header-only library that exposes C++ functions and types in Python, which is also provided with this repository in the `pybind11` directory.
* Header files that contain C++ functions that we want to expose to Python. In this example, the header file `Power.h` contains some sample C++ functions: Square(x), Cube(x), and Power(x, y).
* C++ wrapper file that makes use of the pybind11 headers to expose the C++ functions in our header files to Python. In this example, `PowerPy.cc` is the wrapper file that exposes the C++ functions in `Power.h` header file. Note that the file `PowerPy.cc` also shows a way to provide the documentation for each funtion which can later be accessed from Python.
* A Python script that compiles the C++ wrapper file with our C++ functions and generates a shared object library that can be readily imported as a Python package. In this example, `setup.py` is the Python script that generates a Python library (*PowerPy.xxxx.so*) built out of the C++ functions in `Power.h` header file using the wrapper file `PowerPy.cc` and pybind11 headers in the directory `pybind11`.

(Note: Instead of [pybind11](https://pybind11.readthedocs.io/en/stable/), which is a light-weight header-only library, one can also use Boost-Python from the [Boost](https://www.boost.org/) library which in addition to header files also needs to be installed seperately. The process using Boost-Python instead is a bit more involved, see, e.g., [an earlier version of this repository](https://github.com/prudhvibhattiprolu/PythonifyCpp/tree/1c31901ad7974c51ab23d8b0ee25cb3e1654162d) or a repository at https://github.com/flipdazed/boost-python-hello-world.)

## An example walkthrough

As an example, to build a python package from the C++ functions defined in the header file `Power.h`, first clone this repository via command line by doing

```bash
git clone https://github.com/prudhvibhattiprolu/PythonifyCpp.git
```
For ease of illustration, the header `Power.h` contains the following functions:

 * Square(x): returns square of a number
 * Cube(x): returns cube of a number
 * Power(x, y): returns a number x raised to the power y

which we can expose to Python by doing

```bash
cd PythonifyCpp
python setup.py --quiet build_ext --inplace clean --all
```
The above command compiles the C++ wrapper file `PowerPy.cc` from within the Python script `setup.py` using the [pybind11](https://pybind11.readthedocs.io/en/stable/) header files in the directory `pybind11/include/pybind11/`.
After running the above command, a shared object file of the form *PowerPy.xxxx.so* should appear in the current directory (i.e `PythonifyCpp`) which can then be readily imported into Python. At Python prompt, do:

```python
import PowerPy

PowerPy.Square(4)#To find square of 4
PowerPy.Cube(4)#To find cube of 4
PowerPy.Power(4, 0.5)#To find square-root of 4
```
to start using the C++ code as a Python package!
And the documentation for each function provided in the wrapper file `PowerPy.cc` can be accessed using the Python help function or printed out by doing 

```python
print(PowerPy.Square.__doc__)#To print docstring of the function "Square"
print(PowerPy.Cube.__doc__)#To print docstring of the function "Cube"
print(PowerPy.Power.__doc__)#To print docstring of the function "Power"
```
