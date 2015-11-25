#!/usr/bin/env python
# Project Euler Problem #9
"""
A Pythagorean triplet is a set of three natural numbers.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

def test_triplet(a,b,c):
    return (a**2 + b**2 == c**2)

def calc_triplet(a,b):
    return sqrt(a**2 + b**2)

if __name__ == "__main__":

    c = 1
    b = 1
    done = False
    for a in xrange(1, 1000):
        for b in xrange(1, 1000):
            c = calc_triplet(a,b)
            if a+b+c == 1000:
                print a,b,c
                done = True
                break
            elif a+b+c >1000:
                break
        if done == True:
            break

    print "The triplet whose sum = 1000 is %s, %s, %s, whose product is: %s" %(a,b,c,(a*b*c))
