#!/usr/bin/env python
# Project Euler Problem #15
"""
Starting in the top left corner of a 2 X 2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20 X 20 grid?
"""
from math import factorial as fac

def solve_grid(nSquares):  #nCr permutation
    n = 2*nSquares
    r = nSquares
    return fac(n)/(fac(r)*(fac(n-r)))

if __name__ == "__main__":

    #test
    if solve_grid(2) == 6:
        print "Test passed."
    else:
        print "Test failed!"

    result = solve_grid(20)

    print "The answer to #15 is %s:" %result 

