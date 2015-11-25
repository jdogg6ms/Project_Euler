#!/usr/bin/env python
# Project Euler Problem #24
"""
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations

def lex_perm(number,index):
    list = sorted([''.join(item) for item in permutations(number,len(number))])
    return list[index-1]

if __name__ == "__main__":

    #test
    if lex_perm('102', 6) == '210':     
        print "Test passed."
    else:
        print "Test failed!"

    result = lex_perm('0123456789', 1000000)
    print "The answer to #24 is %s:" %result 

