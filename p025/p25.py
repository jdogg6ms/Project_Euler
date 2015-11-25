#!/usr/bin/env python
# Project Euler Problem #25
"""
The 12th term, F12, is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibCount(n):
    a = 1
    b = 1
    count = 2
    while len(str(b)) < n:
        a, b = b, a + b
        count += 1
    return count


test = 3
if fibCount(test) == 12:
    print "Test passed."
else:
    print "Test failed!"

n = 1000
print "The first term in the Fibonacci sequence to contain 1000 digits is:%s"\
                                                            % fibCount(n)
