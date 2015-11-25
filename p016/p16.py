#!/usr/bin/env python
# Project Euler Problem #16
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def sumPower(num):
    string = str(num)
    return sum(map(int,[char for char in string]))

if __name__ == "__main__":

    try:
      assert 26 == sumPower(2**15)
      print "Test passed."
      result = sumPower(2**1000)
      print "The sum of the digits of the number 2^1000: %s" %(result)

    except:
      print "Test Failed! 26 != %s" %(sumPower(2,15))
