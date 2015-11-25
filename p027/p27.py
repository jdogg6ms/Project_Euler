#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #27

"""
Euler published the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
from  math import sqrt

def euler_quad(a,b):
    # n² + an + b, where |a|< 1000 and |b|< 1000 
    n =0
    while 1:
        value = n**2 + a*n + b
        if not isPrime(value):
            return n 
        n+=1    

def isPrime(n): ## brute force
    if n < 2:
        return False
    elif n == 2: 
        return True
    elif n % 2 ==0:
        return False
    else: 
        x = 3
        limit = int(sqrt(n))+1    
        while x <= limit:
            if n % x == 0:
                return False
            x+=2
        return True 
        
if __name__ == "__main__":

    #test 
    if euler_quad(1,41) == 40 and euler_quad(-79,1601) == 80:
        print "Test passed."
    else:
        print "Test failed!"
    
    max_value = 0
    for a in xrange(-1000,1000):
        for b in xrange(-1000,1000):
            quad = euler_quad(a,b)
            if quad > max_value:
                max_value = quad
                result = a*b  
    print "The answer to #26 is:%s" % result
