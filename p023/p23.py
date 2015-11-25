#!/usr/bin/env python
# Project Euler Problem #23

'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def find_factors(num):
    return [factor for factor in xrange(1,num-1) if num % factor == 0]
 
def isAbundant(num):
    if sum(find_factors(num)) > num:
        return True
    else:
        return False
        
def isDeficient(num):
    if sum(find_factors(num)) < num:
        return True
    else: 
        return False
       
if __name__ == "__main__":
    #test
    if not isAbundant(28) and not isDeficient(28):
        print "test 1 passed."
    else:
        print "test 1 failed!"    
    if isAbundant(12) and not isDeficient(12):
        print "test 2 passed."
    else:
        print "test 2 failed!"    
    
    for i in xrange(1,100):
        if isAbundant(i):
            if i == 12:
                print "test 3 passed."
                break

    remainders = set(xrange(1,28123))
    abundant_list = [x for x in xrange(12,28123) if isAbundant(x)]
    
    for i in abundant_list:
        for j in abundant_list:
            if i+j in remainders:
                remainders.remove(i+j)
    
    print "The answer to #23 is: %s" %sum(remainders)

  
    
    
    
    
    
