#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #40
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

def find_digit(n):
    # returns digit of index n in string concatonation of digits 1 - n    
    s = ''.join([`num` for num in xrange(1,n+1)])
    return int(s[n-1])
             
if __name__ == "__main__":

    #test
    if find_digit(12) == 1:
        print "Test passed."
    else:
        print "Test failed!"
    
    result = 1
    for i in range(6+1):
        print find_digit(10**i)
        result*= find_digit(10**i)

    print "The answer to #40 is:%s" % result
