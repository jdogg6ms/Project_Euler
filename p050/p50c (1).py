exit()#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #50
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import sys
from numba import jit

sys.path.append('/usr/lib/python2.7/site-packages/')

def gen_primes(max_n):
    #sundaram
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

@jit
def consecutive_primes(n_max):
    primes = gen_primes(n_max)
    max_count = 1
    for i in xrange(len(primes)):
        count = 1
        total = primes[i]    
        for j in xrange(i+1,len(primes)):
            total += primes[j]
            count += 1
            if total >= n_max:
                break
            elif total in primes:
                if count > max_count:
                    max_count = count
                    result = total
    return result

if __name__ == "__main__":
    
    #test
    if consecutive_primes(100) == 41 and consecutive_primes(1000) == 953:
        print "Test #1 passed."
    else:
        print "Test #1 failed!"
        
    result = consecutive_primes(1000000)
    print "The answer to 50 is:%s" % result
