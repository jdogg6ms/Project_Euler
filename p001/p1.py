#! /usr/bin/env python
# Project Euler Problem #1

if __name__ == "__main__":
    
    result  = sum([i for i in xrange(3,1000) if i%3 == 0 or i%5 == 0])

    print "The sum of all natural numbers <1000 and divisible by 3 or 5 is: %s" %result
