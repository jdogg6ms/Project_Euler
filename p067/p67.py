#!/usr/bin/env python
# Project Euler Problem #18
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

def sum_route(triangle):
    triangle.reverse()
    length =len(triangle)
    for i in xrange(1,length,1):
        for idx, item in enumerate(triangle[i]):
            if triangle[i-1][idx] > triangle[i-1][idx+1]:
                triangle[i][idx] += triangle[i-1][idx]
            else:
                triangle[i][idx] += triangle[i-1][idx+1]
    return triangle[length-1][0]    
      
    
if __name__ == "__main__":
    #test

    
    with open('p67test_input.txt','r') as test_input:
        test_triangle = []
        for line in test_input: 
            test_triangle.append(map(int,line.split()))
    
    if sum_route(test_triangle) == 23:
        print "Test #1 passed."
    else:
        print "Test #1 failed!"

    
    
    with open('triangle_input.txt','r') as test_input:
        triangle = []
        for line in test_input: 
            triangle.append(map(int,line.split()))

    result = sum_route(triangle)

    print "The answer to #67 is: %s" %result 
