#!/usr/bin/env python
# Project Euler Problem #104
"""
It turns out that F541, which contains 113 digits, is the first Fibonacci number
for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9,
but not necessarily in order). And F2749, which contains 575 digits, is the first
Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
"""

from multiprocessing import Process, Queue, Pool, cpu_count

def fibGen(n):
    a = 1
    b = 1
    count = 2
    while count < n:
        a, b = b, a + b
        count += 1
    return count, b

def fibGenl(n):
    a = 1
    b = 1
    l = [1,1]
    count = 2
    while count < n:
        a, b = b, a + b
        count += 1
        l.append(b)
    l.append(b)    
    return l

def fibGenPD():
    a = 1
    b = 1
    count = 2
    while True:
        if count % 10000 == 0: print count
        if isPandigitalLast9(b):
            if isPandigitalFirst9(b):
                break
        a, b = b, a + b
        count += 1
    return count, b

def isPandigitalFirst9(value):
    #test if first 9 characters include 1-9
    testSet = set('123456789') 
    list = set(str(value)[:9])
    if len(list) < 9:
        return False
    elif '0' in list:
        return False
    elif list == testSet:
        return True
    else:
        return False

def isPandigitalLast9(value):
    #test if last 9 characters include 1-9
    valueTest = value %1000000000 
    testSet = set('123456789') 
    list = set(str(valueTest)[-9:])
    if len(list) < 9:
        return False
    elif '0' in list:
        return False
    elif list == testSet:
        return True
    else:
        return False
    
if __name__ == '__main__':

    fibGen(350000)
