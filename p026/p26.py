#!/usr/bin/env python
# Project Euler Problem #26
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


from decimal import Decimal, getcontext
getcontext().prec = 998

def count_repeating(n,m):
    count = {}
    sub_string = []
#    l = [char for char in str(n/m).lstrip('0.')]
    s = str(Decimal(n)/Decimal(m)).lstrip('0.')
#    print s
    for char in s:
        count[char] = s.count(char)    
    max_count = max(count.values())
#    print max_count
    for item,key in count.iteritems():
        if key == max_count:
            sub_string.append(item)    
    return sub_string   


def gen_primes(max_n):
    #sundaram
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4
    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)
        if initial > half:
            return [2] + filter(None, numbers)
     
        
if __name__ == "__main__":

    #test 
    if len(count_repeating(1,7)) == 6:
        print "Test passed."
    else:
        print "Test failed!",count_repeating(1,7)
    max_length = 0
    for i in gen_primes(1000-1):
        print i, count_repeating(1,i)
#        if len(count_repeating(1,i)) >= max_length:
#            max_length = len(count_repeating(1,i))
#            result = i
##            print i,",", len(count_repeating(1,i)),",",count_repeating(1,i)
    print "The answer to #26 is:%s" % result
