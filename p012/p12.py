#!/usr/bin/env python
# Project Euler Problem #12
"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
from math import sqrt

def divisors(num):
    count = 0
    limit = int(sqrt(num))
    if num % 2 == 0:
        for i in xrange(1,limit):
            if num % i == 0:
                count+=2
    else:
        for i in xrange(1,limit,2):
            if num % i == 0:
                count+=2
    return count

if __name__ == "__main__":

    #test
    if divisors(28) > 5 :
        print "Test #1 passed."
    else:
        print "Test #1 failed!"

    #find first triangle number to have over five hundred divisors
    count = 0
    triangle = 0
    while divisors(triangle) < 500:
        count+=1
        triangle += count

    result = triangle

    print "The answer to #12 is: %s" %result
