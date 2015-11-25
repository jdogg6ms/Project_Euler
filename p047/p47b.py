#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #47
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2²  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
"""
from math import sqrt

def consecutive_factors(nConsecutive,nPrimeFactors):
    # returns a list of first consecutive numbers that meet criteria
    i = 4
    done = False
    while not done:
        output_list = []
        for num in xrange(i,i+nConsecutive):
            if len(PrimeFactors(num,nPrimeFactors)) < nPrimeFactors:
                i = num+1
                done = False
                break
            else:
                output_list.append(num)
                done = True
    return output_list        
                
                
def PrimeFactors(n,nPrimeFactors):
    # returns a list of factors of n that are prime
    return [x for x in gen_primes(int(n/nPrimeFactors)+1) if n%x==0 and n!=x]
        
def gen_primes(max_n):
    #sundaram sieve for generating primes
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4
    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)
        if initial > half:
            return [2] + filter(None, numbers)

if __name__ == "__main__":

    #test
    if consecutive_factors(2,2) == [14,15]\
    and consecutive_factors(3,3) == [644,645,646]: 
        print "Test passed."
    else:
        print "Test failed!",consecutive_factors(2,2),consecutive_factors(3,3)

    result = consecutive_factors(4,4)[0]

    print "The answer to #47 is:%s" % result
