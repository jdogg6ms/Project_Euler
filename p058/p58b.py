#!/usr/bin/env python
# Project Euler Problem #58
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13  62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""
from math import sqrt

def find_diagonals(n):
    # corner value = odd number^2
    corner_values = [1]
    for i in xrange(3,n+1,2):
        step = i-1
        corner = i**2
        for i in xrange(0,3+1):
            corner_values.append(corner-step*i)
    return corner_values

def sundaram(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def sundaramIsPrime(n,primeSet): ## check only for multiples of primes
    if n in primeSet:
        return True
    elif n < 2:
        return False    
    else:
        return False
        
def precent_prime(n):
    l = find_diagonals(n)
    primeSet = sundaram(n**3)
    return round(float(len([x for x in l if sundaramIsPrime(x,primeSet)]))/float(len(l)),2)


if __name__ == "__main__":

    #test
    if precent_prime(7) == 0.62:
        print "Test passed."
    else:
        print "Test failed!", precent_prime(7)
    
    i = 7
    while precent_prime(i) >=0.1:
        i+=1
         
    print "The answer to #58 is:%s" % i
