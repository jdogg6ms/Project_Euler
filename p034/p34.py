#!/usr/bin/env python
# Project Euler Problem #30

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial
 
def isSumOfFactorials(num):
    if num == sum(map(factorial,[int(char) for char in str(num)])):
        return True
    else:
        return False

''' how far to test for 'all' numbers?  Since the number of digits in the
    sum must equal the number of digits in the number with a little testing
    we notice that the highest 8 digit number (99,999,999) has a factorial 
    sum 7 digits long. Thus to ensure all answers are found we test to 8 places
    or 10**7 = 10000000
'''

def find_range():
    i = 1
    while len(str(i*factorial(9))) >= i:
        i+=1
    return 10**(i-1)
       
if __name__ == "__main__":
    #test
    if isSumOfFactorials(145):
        print "test passed."
    else:
        print "test failed!"    
   
    print find_range()
    result = sum([num for num in xrange(3,find_range()) if isSumOfFactorials(num)])
    
        
    print "The answer to #34 is: %s" % result

  
    
    
    
    
    
