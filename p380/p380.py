#! /usr/lib/env Python
# Project Euler #380
from math import factorial

def num_walls(n,m):
  return (n-1)*(m-1)  #r

def num_wall_locations(n,m):
  return 2*m*n-m-n     #P

def num_possible_solutions(n,m):
  P = num_wall_locations(n,m)
  r = num_walls(n,m)
  
  return factorial(P)/(factorial(r)*factorial(P-r))

def num_invalid_wall_locations(n,m):
  return 0

for i in range(2,5):
  print "for a %s x %s there are %s walls and %s possible locations"\
                               %(i,i,num_walls(i,i),num_wall_locations(i,i))  
  print "for a %s x %s the number of possible combinations is %s\n"\
                               %(i,i,num_possible_solutions(i,i))  
