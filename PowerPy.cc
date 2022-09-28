//Pybind11 header files that expose C++ functions to Python
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

//Include the header files that contain the C++ (lambda) functions that we want
//to expose to Python.
#include "Power.h"//provides our functions: Square(x), Cube(x), and Power(x, y)

namespace py = pybind11;

PYBIND11_MODULE(PowerPy, mod)
{
    mod.def(
            //Name of the function to appear in Python
            "Square",
            //Call the C++ function to be exposed to Python
            &Square,
            //Documentation for this function that appears as a Python docstring
            R"pbdoc(
            returns square of a number
            )pbdoc",
            //List of arguments with their names seperated by commas
            py::arg("x")
            );

    mod.def("Cube", &Cube,
            R"pbdoc(
            returns cube of a number
            )pbdoc",
            py::arg("x")
            );

    mod.def("Power", &Power,
            R"pbdoc(
            returns x raised to a power y
            )pbdoc",
            py::arg("x"), py::arg("y")
            );

};
