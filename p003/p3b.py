#!/usr/bin/env python
# Project Euler Problem #3
from math import sqrt
num = 600851475143
prime_factors = []
result = 1

def isPrime(n):
    if n < 2:
        return False
    elif n == 2: 
        return True    
    elif n % 2 ==0:
        return False
    else:
        x = 3    
        while x < sqrt(n):
            if n % x == 0:
                return False
            x+=2
    return True


if __name__ == "__main__":

    for i in range(int(sqrt(num))+1,2,-1):  
        if num % i == 0:   
            factor = num / i
            if isPrime(i):
                if i > result:
                    result = i
            if isPrime(factor):
                if factor > result:
                    result = factor
    if result == 1:   
        result = num
                      
    print "The largest prime factor of %s is: %s" %(num,result)
