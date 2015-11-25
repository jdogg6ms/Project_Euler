#!/usr/bin/env python
# Project Euler Problem #5
# find smallest number that can be evenly divided by 1-20

def test_factor(n):
  for i in range(11, 20):
    if n % i !=0:
      return False
    else:
      None
  return True

if __name__ == "__main__":

    i = 0
    result = 0
    while result == 0:
        i+=20
        if test_factor(i):
            result = i


    print "The smallest number evenly divided by 1-20 is: %s" %(result)

