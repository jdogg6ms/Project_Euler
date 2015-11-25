#!/usr/bin/env python
# Project Euler Problem #6
"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sums_squared(n):
  # Calculates the sum of squared of numbers from 1 to n
  return sum([x**2 for x in xrange(1,n+1)])
    
def square_of_sums(n):
  # Calculates the squared sum of numbers from 1 to n
  return sum([x for x in xrange(1,n+1)])**2

if __name__ == "__main__":
  import math


  try: #verify alogrithm
    test = 10
    assert 2640 == square_of_sums(test)-sums_squared(test)
    print "Test case passed.\n"

    n = 100
    delta = square_of_sums(n) - sums_squared(n)
    print "The difference between squared sums and sum of squares is: %s" %(delta)

  except:
    print "Test Case failed! %s !=2640" %(square_of_sums(test) - sums_squared(test))
