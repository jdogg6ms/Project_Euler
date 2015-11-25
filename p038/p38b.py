#!/usr/bin/env python
# Project Euler Problem #38
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n >1?
"""
from itertools import permutations

def find_product(n,m):
    string = ''
    for i in xrange(1,m+1):
        string = "%s%s" % (string,n*i)
    return string

def test_product(s):
    for i in xrange(len(s)):
        for j in xrange(i,len(s)+1):  
            if s[:i]+s[i:j] = int(s[j:])
                return True
    return False    

if __name__ == '__main__':

    #test functions
    if isPandigital2(find_product(9,5)) and isPandigital2(find_product(192,3)):
        print "Test passed.\n"
    else:
        print "Test failed!"
       
    [''.join(item) for item in permutations('123456789',9)]
            
    print "The answer to # 38 is: %s" % result
