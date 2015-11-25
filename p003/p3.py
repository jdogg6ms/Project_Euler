#!/usr/bin/env python
# Project Euler Problem #3

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

from math import sqrt
prime_factors = []
result = 1

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 ==0:
        return False
    x = 3
    limit = int(sqrt(n))+1
    while x < limit:
        if n % x == 0:
            return False
        x+=2
    return True

if __name__ == "__main__":

    num = 600851475143
    for i in range(int(sqrt(num))+1,2,-1):
        if num % i == 0:
            factor = num / i
            if isPrime(i):
                result = max([i,result])
            if isPrime(factor):
                result = max([factor,result])
    if result == 1:
        result = num

    print "The largest prime factor of %s is: %s" %(num,result)

