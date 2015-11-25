#!/usr/bin/env python
# Project Euler Problem #20
"""
n! means n  (n  1)  ...  3  2  1
For example, 10! = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""
def sumFactorial(n):
    from math import factorial
    return sum([int(char) for char in str(factorial(n))])

if __name__ == "__main__":
  
    try:
      assert 27 == sumFactorial(10)
      print "Test passed."
      result = sumFactorial(100)                         
      print "The sum of the digits in the number 100!: %s" %(result)

    except:
      print "Test Failed! 27 != %s" %(sumFactorial(10))
  
 

  
  



