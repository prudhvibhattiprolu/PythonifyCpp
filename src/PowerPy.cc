//To build:
//  >>> python setup.py --quiet build_ext --inplace clean --all

//C++ functions to be exposed to Python.
//For ease of illustration, the function "square" return the square of a number, and "cube" returns cube of a number.
//(The functions can also be defined in a header file and then be included here)
double square(double x)
{
   return x*x;
}

double cube(double x)
{
   return x*x*x;
}

#define BOOST_BIND_GLOBAL_PLACEHOLDERS
#include <boost/python.hpp>//Include Boost-Python library

BOOST_PYTHON_MODULE(PowerPy)
{
    using namespace boost::python;

    //Exposing the C++ functions (after "&" below) to Python with the corresponding names given in quotes.
    //If need be there is a way to write docstring here.
    //Instead, as is done in this repository, it might be more convenient to input docstring in __init__.py file in the src directory structure.

    def("square", &square);
    
    def("cube", &cube);
};

