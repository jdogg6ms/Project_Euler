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
from math import factorial, sqrt

primeSet  = set([2,3])
primeList = [2,3]   

def isPrime(n,primeSet, primeList):
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

def S(p):      
    return sum([factorial(p-k) for k in range(1,5+1)])%p
        
if __name__ == "__main__":
    #verify test problem
    if S(7) == 4:
        print "test #1 passed."
    else:
        print "test failed!" 
    
    if sum([S(p) for p in range (5,100) if isPrime(p,primeSet, primeList)]) == 480:    
        print "test #2 passed."
    else:
        print "test failed!"     
        
    result = sum([S(p) for p in xrange(5,100000000,2) if isPrime(p,primeSet, primeList)])  
    print "The answer to #381 is: %s" %result 
