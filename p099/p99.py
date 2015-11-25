#!/usr/bin/env python
#Project Euler Problem #99

"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 2^11 = 2048  3^7 = 2187.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
from math import log

def calc_log(s):
    l = map(int,s.split(','))
    return l[1]*log(l[0])


if __name__ == "__main__":
    
    #test
    if calc_log('2,11') < calc_log('3,7'):
        print "Test passed."
    else:
        print "Test failed!"    
    

    #find largest value in base_exp.txt
    lines = map(calc_log,[line.strip('\n') for line in open('base_exp.txt', 'r')])
    result = lines.index(max(lines))+1
    
    print "The answer to #99 is: %s" % result 
    
