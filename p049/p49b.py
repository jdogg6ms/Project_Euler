#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #49
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
ANS=296962999629
    379937993799
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
    
    for num in [x for x in xrange(1001,10000,2) if isPrime(x)]:
        
        perms_notprime =[int(''.join(combo)) for combo in permutations(str(num),4)]
        
        perms = sorted([x for x in perms_notprime if x>1000 and isPrime(x)])        
        
        if len(perms) < 3:
            None
        else:
#            print perms
            done = False
            for i in xrange(len(perms)):
                if done == True:
                    break
                for j in xrange(i+1,len(perms)):
                    if (perms[j]+ (perms[j] - perms[i])) in perms\
                    and perms[i] != perms[j]:
                        print "found =>", perms[i], perms[j], (perms[j] + (perms[j] - perms[i]))
                        
                        result = "%s%s%s" % (perms[i], perms[j], (perms[j] + (perms[j] - perms[i])))
                        done = True
                        break
                    else:
                        None
    print "The answer to 49 is:%s" % result
