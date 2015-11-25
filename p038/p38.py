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

def find_product(n,m):
    string = ''
    for i in xrange(1,m+1):
        string = "%s%s" % (string,n*i)
    return string
    
def isPandigital(string):
    #test if 9 characters include 1-9
    if type (string) != str:
        string = '%s' %(string)
    length = len(string)
    if length < 9:
        return False 
    if set(string) == set('123456789'):
        return True
    else:
        return False 

if __name__ == '__main__':

    #test functions
    if isPandigital(find_product(9,5)) and isPandigital(find_product(192,3)):
        print "Test passed.\n"
    else:
        print "Test failed!"
    
#    [int(x) for x in xrange(1,100000) if isPandigital(find_product(x))]
    
    i = 1
    product = '0'
    result = 0
    for i in xrange(1,10000000):
        for j in xrange(1,10000000):
            product = find_product(i,j)
            length = len(product)
            if length > 9:
                break
            if isPandigital(product):
                value = int(product)
                if value > result:
                    result = value 
            
    print "The answer to # 38 is: %s" % result
