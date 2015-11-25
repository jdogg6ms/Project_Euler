#!/usr/bin/env python
# Project Euler Problem #4
# find largest pallidrome as product of (2) 3-digit numbers


if __name__ == "__main__":

    nVals = 2
    nDigits = 3
    max_value = int('9'*nDigits)**nVals
    done = False

    for i in range(max_value,1,-1):
        if str(i) == str(i)[::-1]:
            for j in range(10**nDigits,1,-1):   
                if i%j == 0 and j < 10**nDigits and i/j < 10**nDigits:
                    print i,j, i/j    
                    result = i
                    done = True
                    break
        if done == True: 
            break            
    print "The largest pallidrome of (%s) %s-digit numbers  is: %s" %(nVals, nDigits, result)

