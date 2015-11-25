#!/usr/bin/env python
# Project Euler Problem #5
# find smallest number that can be evenly divided by 1-20

from multiprocessing import Queue, Pool, cpu_count
pool = Pool(processes=cpu_count()) 

def test_factor(n):
  for i in range(2,21):
    if n % i !=0:
      return False
  else:
    return True    

if __name__ == "__main__":

  i = 0
  result = 0
  
  for i in xrange(0,100000,20):
    presult = pool.apply_async(test_factor,(i,))
    if presult.get():
        result = i

  print "The smallest number evenly divided by 1-20 is: %s" %(result)

