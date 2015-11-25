#!/usr/bin/env python
# Project Euler Problem #11
"""
What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20 x 20 grid?
(see p11_input.txt)
"""

from array import array
from operator import mul

def row_product(matrix,i,j):
    return reduce(mul,[x for x in matrix[i][j:j+4]]) 

def column_product(matrix,i,j):
    l =[]
    for k in xrange(4):
        try:
            l.append(matrix[i+k][j])
        except IndexError:
            l.append(0)      
    return reduce(mul,l) 
    
def diag_productSE(matrix,i,j):
    l =[]
    for k in xrange(4):
        try:
            l.append(matrix[i+k][j+k])
        except IndexError:
            l.append(0)     
    return reduce(mul,l)     

def diag_productSW(matrix,i,j):
    l =[]
    for k in xrange(4):
        try:
            l.append(matrix[i+k][j-k])
        except IndexError:
            l.append(0)     
    return reduce(mul,l)   

if __name__ == "__main__":
    matrix = []
    result_list = []
    with open('p11_input.txt','r') as input:
        for line in input:
            matrix.append(map(int,line.split()))
        
        #test 1
        if diag_productSE(matrix,6,8) == 1788696:
            print "Test #1 passed."
        else:
            print "Test #1 failed!", diag_productSE(matrix,6,8)
            
        #test 2
        if diag_productSW(matrix,0,4) == 3298400:
            print "Test #2 passed."
        else:
            print "Test #2 failed!", diag_productSW(matrix,0,4) 

        #test 3
        if row_product(matrix,0,0) == 34144:
            print "Test #3 passed."
        else:
            print "Test #3 failed!", diag_productSE(matrix,6,8)
            
        #test 4
        if column_product(matrix,0,0) == 1651104:
            print "Test #4 passed.\n"
        else:
            print "Test #4 failed!", diag_productSW(matrix,0,4)             
               

        for i in xrange(len(matrix[0])):
            for j in xrange(len(matrix)):
                result_list.append(max(row_product(matrix,i,j)\
                ,column_product(matrix,i,j)\
                ,diag_productSE(matrix,i,j)\
                ,diag_productSW(matrix,i,j)))

    result = max(result_list)

    print "The answer to #11 is %s:" %result 

