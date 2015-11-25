#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #31
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?

ANS = 73682
"""
def find_combinations(rem, coins):
    count = 0
    if rem ==0 or coins[0] ==1:
        return 1         
    else:
        for i in xrange((rem / coins[0])+1):
            remainder = rem - i*coins[0]
            count+=find_combinations(remainder, coins[1:])
    return count    

if __name__ == "__main__":

    #test
    coins = [10,5,1]
    if find_combinations(20,coins) == 9: 
        print "Test passed."
    else:
        print "Test failed!"

    coins = [200,100,50,20,10,5,2,1]
    result = find_combinations(200,coins)
    
    print "The answer to #31 is:%s" % result
