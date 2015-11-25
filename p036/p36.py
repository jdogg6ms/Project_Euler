#!/usr/bin/env python
# Project Euler Problem #36
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
def isPalindrome(n):
    if type(n) != 'str':
        n = str(n)       
    if n == n[::-1]:   
        return True
    else:
        return False

if __name__ == "__main__":
    #test
    if isPalindrome(585) and isPalindrome(bin(585).lstrip('0b')): 
        print "test passed."

    else:
        print "test failed!"   

    result = sum([x for x in xrange(1,1000000) if isPalindrome(x) and isPalindrome(bin(x).lstrip('0b'))])
         
    print "The answer to #36 is: %s" %(result)
