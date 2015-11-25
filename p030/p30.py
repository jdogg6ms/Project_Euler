#!/usr/bin/env python
# Project Euler Problem #30

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
from math import pow
 
def isSumOfPowers(num,power):
    g = lambda x: int(pow(x,power))
    if num == sum(map(g,[int(char) for char in str(num)])):
        return True
    else:
        return False

def find_range():
    i = 1
    while len(str(i*pow(9,5))) >= i:
        i+=1
    return 10**(i-2)

       
if __name__ == "__main__":
    #test
    if  isSumOfPowers(1634,4) and isSumOfPowers(8208,4) and \
        isSumOfPowers(9474,4) and not isSumOfPowers(8208,5):
        print "test passed."
    else:
        print "test failed!"    

    result = sum([x for x in xrange(2,find_range()) if isSumOfPowers(x,5)])      
    
    print "The answer to #30 is: %s" %result 
