#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #41
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from math import sqrt

primeSet  = set([2,3])
primeList = [2,3]        

def isPrime2(n,primeSet, primeList): ## check only for multiples of primes
    if n in primeSet:
        return True
    elif n < 2:
        return False    
    else:
        limit = int(sqrt(n))+1    
        for x in primeList: 
            if x >= limit:
                break
            else:
                if n % x == 0:
                    return False
        primeSet.add(n)
        primeList.append(n)
        return True
        
def isPrime(n): ## brute force
    if n < 2:
        return False
    elif n == 2: 
        return True
    elif n % 2 ==0:
        return False
    else: 
        x = 3
        limit = int(sqrt(n))+1    
        while x <= limit:
            if n % x == 0:
                return False
            x+=2
        return True  

def gen_primes(max_n):
    #sundaram
    numbers = range(3, max_n, 2)
    half = (max_n)//2
    initial = 4
    for step in xrange(3, max_n, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)
        if initial > half:
            return [2] + filter(None, numbers)
            
def isPandigital(n):
    #test if characters include digits 1-n
    string = str(n)
    string_len =len(string)
    string_set = set(string)
    if string_len != len(string_set):
        return False
    pan_list = '123456789'[:string_len]
    if string_set == set(pan_list):
        return True
    else:
        return False             

if __name__ == "__main__":

    #test
    if isPrime(2143) and isPandigital(2143): 
        print "Test passed."
    else:
        print "Test failed!"

    # 3:47 run-time pypy
    # 3:47 run-time python    
    result = max([x for x in gen_primes(987654321) if isPandigital(x)]) 

    # 34m7.069s run-time pypy
#    for x in reversed(gen_primes(987654321)):
#        print x
#        if isPandigital(x):
#            result = x 
#            break 
            

#    for x in xrange(987654321,1,-2):
#        if x % 1000001 ==0: 
#            print x  
#        if isPandigital(x) and isPrime2(x,primeSet,primeList):
#            result = x 
#            break             
    
#    for x in xrange(987654321,1,-2):
#        if x % 1000001 ==0: 
#            print x  
#        if isPandigital(x) and isPrime(x):
#            result = x 
#            break   

    print "The answer to #41 is:%s" % result
