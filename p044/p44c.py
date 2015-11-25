#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #44
"""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70  22 = 48, is not pentagonal.
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
"""

from math import sqrt   
  
def isPentagonal(P):
    """
    Pn=n(3n-1)/2
    3n^2/2 +n/2 - P = 0
    a = 3/2
    b = -1/2
    c = -P
    descriminant = b^2 - 4*a*c
    descriminant = (-1/2)**2 - 4*(3/2)*(-P))
    root = (-b+-sqrt(b**2-(4*a*c))/(2*a)
    """
    descriminant = 0.25 - 6*-P
    if descriminant < 0:
        return False
    else:
        root1 = (0.5+sqrt(descriminant))/3
        root2 = (0.5-sqrt(descriminant))/3
        # return true if positive root is an integer
        if root1 % 1 ==0 and root1 >=0 \
        or root2 % 1 ==0 and root2 >=0:
            return True 
        else:
            return False  

def genPentagonalList(n_max,n_start = 1):
    return set([x*(3*x-1)/2 for x in xrange(n_start,n_max+1)])

def pentagonal(x):
    return x*(3*x-1)/2

if __name__ == "__main__":
    
    if isPentagonal(pentagonal(4) + pentagonal(7))\
    and not isPentagonal(pentagonal(4) - pentagonal(7)):
        print "Test passed."
    else:
        print "Test failed!"
    
    maxN = 10**4
    result = 10**6
    for i in xrange(maxN):
        a = pentagonal(i)
        for j in xrange(i+1,maxN): 
            b = pentagonal(j)
            if isPentagonal(a+b) and isPentagonal(a-b):
                if abs(a-b) < result:
                    result = abs(a-b)
                    print result
                    break
                
    print "The answer to #44 is:%s" % result
