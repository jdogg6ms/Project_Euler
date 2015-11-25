#!/usr/bin/env python
# Project Euler Problem #381

'''
For a prime p let S(p) = ((p-k)!) mod(p) for 1 <= k <= 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.
It can be verified that Sum(S(p)) = 480 for 5 <= p < 100.
Find Sum(S(p)) for 5 <=  p < 108.
'''
from math import factorial as fac, sqrt

primeSet  = set([2,3])
primeList = [2,3]   

def isPrime(n,primeSet = None, primeList = None):
    if primeSet == None:
        primeSet  = set([2,3])
        primeList = [2,3]  

    if n in primeSet:
        return True
    elif n < 2:
        return False    
    else:
        limit = int(sqrt(n))+1    
        for x in primeList: 
            if x >= limit:
                break
            else:
                if n % x == 0:
                    return False
        primeSet.add(n)
        primeList.append(n)
        return True

def sundaram(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4 # was 4
    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def S(p):
    value = 0
    #(p-3) term
    value+= (p-1)/2
    #(p-4) term
    if (p+1)%6 ==0:
        value += (p+1)/6
    else:
        value += (5*p+1)/6
    #(p-5) term
    if (p-1)%24 == 0:
        value += (p-1)/24
    else:
        value += ((p**2-1)/24)%p
    return value % p
           
if __name__ == "__main__":
    #verify test problem
    if S(7) == 4:
        print "test #1 passed."
    else:
        print "test failed!", S(7) 
    
    if sum([S(p) for p in range (5,100) if isPrime(p,primeSet, primeList)]) == 480:    
        print "test #2 passed."
    else:
        print "test #2 failed!"     
        
    result = sum([S(p) for p in sundaram(10**8) if p not in [2,3]])  
    print "The answer to #381 is: %s" %result 
