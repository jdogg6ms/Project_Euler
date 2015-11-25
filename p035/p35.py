#!/usr/bin/env python
# Project Euler Problem #35

'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
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

def isCircPrime(n):
    list = [x for x in str(n)]
    for i in xrange(len(list)):
        list.append(list.pop(0))
        if not isPrime(int(''.join(list))): 
            return False
    return True

if __name__ == "__main__":
    #test
    if isCircPrime(197):  # and not isCircPrime(345):
        print "test passed."
    else:
        print "test failed!"    
    
    # find the length of all odd circular primes from 3 to 1 mil.
    # +1 added for the number 2      
    result = len([i for i in range(3,1000000,2) if isCircPrime(i)])+1       
  
    print "The answer to #35 is: %s" % result

    
