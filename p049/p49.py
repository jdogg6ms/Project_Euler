#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #49
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from math import sqrt 
from itertools import permutations  

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
    
    for num in [x for x in xrange(1000,10000) if isPrime(x)]:
        perms =[int(''.join(item)) for item in permutations(str(num),4)]
            if len(perms) < 3:
                continue
            else:
              for i in xrange(len(perms)):
                print item[i]
                for j in xrange(i+1,len(perms)):
                    if (item[i]+ (item[j] - item[i])) in perms:
                         result = item[i] + item[j] + (item[i] + (item[j] - item[i]))
                
#    print "The answer to 49 is:%s" % result
