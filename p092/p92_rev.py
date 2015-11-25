#!/usr/bin/env python
#Project Euler Problem #92

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89

How many starting numbers below ten million will arrive at 89?
"""
def digits_squared(n):
    return sum([int(char)**2 for char in str(n)])

def is89(n, true_set,false_set,temp_set = set()):
    if n in true_set:
        return True
    elif n in false_set:
        return False    
    elif digits_squared(n) == 1:
        temp_set.add(n)
        for item in temp_set:
            false_set.add(item)
        return False
    elif digits_squared(n) == 89:
        temp_set.add(n)
        for item in temp_set:
            true_set.add(item)
        return True       
    else:       
        temp_set.add(n)
        is89(digits_squared(n),true_set,false_set,temp_set) 
               


if __name__ == "__main__":
    true_set = set()
    false_set = set()
    
    #test
    if not is89(44,true_set,false_set) and is89(85,true_set,false_set):
        print "Test passed."
    else:
        print "Test failed!"    
    
    count = 0
    for x in xrange(10000000,2,-1):
        if x % 10000==0: print x
        if is89(x,true_set,false_set):
            count+=1    
         
#    result = len([x for x in xrange(2,10000000) if is89(x,true_set,false_set)]) 
    print "The answer to #92 is: %s" % count
