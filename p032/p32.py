#!/usr/bin/env python
# Project Euler Problem #32

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
 
def isPandigital(factor1, factor2):
    #test if 9 characters include 1-9
    list = '%s%s%s' %(factor1,factor2,factor1*factor2)
    if len(list) != 9:
        return False
    if set(list) == set('123456789'):
        return True
    else:
        return False 
       
if __name__ == "__main__":
    #test
    if isPandigital(39,186) and not isPandigital(32,48):
        print "test passed."
    else:
        print "test failed!"    
    
    products = set([])
    for i in xrange(2,100):
        if '0' not in str(i):
            for j in xrange(100,5001):
                if '0' not in str(j): 
                    if isPandigital(i,j):
                        print i,"*", j,"=", i*j
                        products.add(i*j)
                        
    result = sum(products)
  
    print "The answer to #32 is: %s" % result

#Notes  
''' The first loop runs from 2 to 100 because 2 is the first possible factor
    and 100 is the sqrt(9999) the highest 4 digit number that should bound the 
    product. 

    The second loop runs from 70 to 5000 because the highest 4 digit number
    9999 / 2 = 4999.5.  This should be the highest that one can go to be able
    to figure out all factors before tripping the product over to 6 digits. 
    100 is chosen as the loop start because it is the sqrt(9999)
'''    
    
    
