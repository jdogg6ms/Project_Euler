#!/usr/bin/env python
# Project Euler Problem #21
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from math import sqrt

def sumDivisors(n):
    divisors = set([1])
    for i in xrange(2,int(sqrt(n)+2)):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n/i)
    return sum(divisors) 
    
def hasAmicablePair(n):
    m = sumDivisors(n)
    if sumDivisors(m) == n and n != m:
        return True
    else:
        return False    
            
if __name__ == "__main__":
    #test
    if hasAmicablePair(220) and hasAmicablePair(284) and not hasAmicablePair(89):
        print "test passed."
    else:
        print "test failed!"   
   
    result = sum([x for x in xrange(1,10000) if hasAmicablePair(x)])
  
    print "The answer to 21 is: %s" %(result)
