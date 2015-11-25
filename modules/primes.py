#!/usr/bin/env python
# Prime testing 
from __future__ import generators
from math import sqrt
from time import time
 
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

primeSet  = set([2,3])
primeList = [2,3]        

def isPrime2(n,primeSet, primeList): ## check only for multiples of primes
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

def sundaramIsPrime(n,primeSet): 
    if n in primeSet:
        return True
    elif n < 2:
        return False    
    else:
        return False

       
if __name__ == "__main__":

    maxRange = 10**7
    print "For odd range of %s" % maxRange

    t = time() 
    p1 =[x for x in xrange(1,maxRange) if isPrime(x)]
    print len(p1), "Prime\t= %s seconds" %(time()-t)

    t = time()
    p2 = [2]+[x for x in xrange(3,maxRange,2) if isPrime2(x,primeSet, primeList)]
    print len(p2), "Prime2\t= %s seconds" %(time()-t)

#    t = time()
#    p3 = gen_primes(maxRange)
#    print len(p3), "sundaram\t= %s seconds" %(time()-t)

    t = time()
    primeSet= set(gen_primes(maxRange))
    p4 = [2]+[x for x in xrange(3,maxRange,2) if sundaramIsPrime(x,primeSet)]
    print len(p4), "sundaramIsPrime\t= %s seconds" %(time()-t)
