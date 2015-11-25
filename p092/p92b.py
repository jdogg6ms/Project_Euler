#!/usr/bin/env python
#Project Euler Problem #92

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89

How many starting numbers below ten million will arrive at 89?
"""
def divisors(n):
    return None

def expand89(n, set89 = set()):
    if len(set89) == 0:
        set89 = set('89')
    while len(set89) <n:
        
        
        

    return 
    
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
        
    print "The answer to #92 is: %s" % result 
