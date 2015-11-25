#!/usr/bin/env python
#Project Euler Problem #33

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from operator import mul

def isUnorthodox(n,m):
    for char in str(n):
        if char in str(m):
            num = float(str(n).replace(char,'',1))
            denom = float(str(m).replace(char,'',1))
            if num/denom == float(n)/float(m):
                return True
    return False

def reduce_fraction(numerator,denominator):
    for num in xrange(numerator,1,-1):
        if numerator % num == 0 and denominator % num ==0:
            numerator   /= num 
            denominator /= num 
    return (numerator,denominator)


if __name__ == "__main__":

    #test
    if isUnorthodox(49,98) and not isUnorthodox(47,94):
        print "Test passed."
    else:
        print "Test failed!"
        
    results = []
    for i in xrange(11,100):
        if i %10 !=0:
            for j in xrange(11,100):
                if j %10 != 0 and i != j:
                    if i > j:
                        None
                    elif isUnorthodox(i,j):
                        results.append([i,j])
                        
    print "The four solutions are : ", results
    
    numerator   = reduce(mul,[item[0] for item in results])
    denominator = reduce(mul,[item[1] for item in results])
    numerator, denominator = reduce_fraction(numerator,denominator)
                
    print "Reduced solution = %s/%s" %(numerator,denominator)
