#!/usr/bin/env python
#Project Euler Problem #97

"""
Find the last ten digits of the prime number 28433 x 2^7830457+1.
"""

if __name__ == "__main__":
    
    result = (28433*(2**7830457)+1)%10**10
    
    print "The answer to #97 is: %s" % result 
    
