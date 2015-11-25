#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #39
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
"""
from math import sqrt
        
def calc_parameter(a,b):
    return a + b + sqrt(a**2+b**2)
    
def count_triplets(p):
    solution_count = 0
    for a in range(1,p):
        for b in range(a+1,p):
            if p == calc_parameter(a,b):
                solution_count+=1
    return solution_count
            
if __name__ == "__main__":

    #test
    if count_triplets(120) == 3:
        print "Test passed."
    else:
        print "Test failed!"
    
    max_solutions = 0
    for i in xrange(1,1000+1):
        soln = count_triplets(i)
        if soln > max_solutions:
            max_solutions = soln
            result = i

    print "The answer to #39 is:%s" % result
