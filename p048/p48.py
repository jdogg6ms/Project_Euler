#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #48
"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from math import pow   
  
def last_ten(x):
    return (sum([x**x for x in xrange(1,x+1)]))%10000000000
    
if __name__ == "__main__":
    
    if last_ten(10) == 405071317:
        print "Test passed."
    else:
        print "Test failed!",last_ten(10)
    
    result = last_ten(1000)
                                    
    print "The answer to #48 is:%s" % result
