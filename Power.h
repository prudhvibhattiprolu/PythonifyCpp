//C++ functions to be exposed to Python. For ease of illustration, consider the
//following functions:
//
// * Square(x): returns square of a number
// * Cube(x): returns cube of a number
// * Power(x, y): returns a number x raised to the power y
//
//that are defined below.
//
#ifndef POWER_H
#define POWER_H

//Include header files needed to define our functions
#include <cmath>/*provides pow*/

//Square a number x
double Square(double x)
{
   return x*x;
}

//Cube a number x
double Cube(double x)
{
   return x*x*x;
}

//Raise a number x to a power y
double Power(double x, double y)
{
   return pow(x, y);
}

#endif
