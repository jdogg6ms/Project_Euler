#!/usr/bin/env python
# Project Euler Problem #37

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import math
 
def isPrime(n):
    if n < 2:
        return False
    elif n == 2: 
        return True
    elif n % 2 ==0:
        return False
    else: 
        x = 3    
        while x < int(math.sqrt(n))+1:
            if n % x == 0:
                return False
            x+=2
        return True

def isTruncPrime(n):
    listR = [x for x in str(n)]
    listL = [x for x in str(n)]
 
    for i in xrange(len(listR)):
 
        if not isPrime(int(''.join(listR))): 
            return False
 
        if not isPrime(int(''.join(listL))): 
            return False   
        listR.pop()  
        listL.pop(0)
    return True

if __name__ == "__main__":
    #test
    if isTruncPrime(3797): 
        print "test passed."
    else:
        print "test failed!"    
    
    i = 11
    trunc_primes = []
    while len(trunc_primes) <11:
        if isTruncPrime(i):
            trunc_primes.append(i)
        i+=2
  
    print "The answer to #37 is: %s" % sum(trunc_primes)

    
