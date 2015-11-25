#!/usr/bin/env python
# Project Euler Problem #46

'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9  = 7 +  2*1^2
15 = 7 +  2*2^2
21 = 3 +  2*3^2
25 = 7 +  2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from math import pow, sqrt

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

def isComposite(num):
    for sq in xrange(1,num): #square term
        if num - 2*sq**2 <2:
            return False
        elif isPrime(num- 2*sq**2):
            return True
    return False
        
if __name__ == "__main__":
    #test
    if isComposite(33) and isComposite(9):
        print "test passed."
    else:
        print "test failed!"    

    for odd in [x for x in xrange(9,10**6,2) if not isPrime(x)]:
        if not isComposite(odd):        
            result = odd
            break
  
    print "The answer to 46 is: %s" % result

    
    
