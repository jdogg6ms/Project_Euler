#!/usr/bin/env python
# Project Euler Problem #28
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def diagonalSum(n):
    # corner value = odd number^2
    return 1 + sum([ 4*(i**2)-6*(i-1) for i in xrange(3,n+1,2)]) 

if __name__ == "__main__":

    #test
    if diagonalSum(5) == 101:
        print "Test passed."
    else:
        print "Test failed!"

    result = diagonalSum(1001)

    print "The answer to #28 is:%s" % result
