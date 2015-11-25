#!/usr/bin/env python
# Project Euler Problem #2
sum = 0
a = 1
b = 1
while a < 4000000:
    a, b = b, a + b
    if a % 2 == 0:
        sum += a 

print "The sum of even values of fib sequence under 4 million is:%s" %sum

