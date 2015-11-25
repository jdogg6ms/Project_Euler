#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler Problem #42
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
def isTriangle(n):
    if n in [int(0.5*x*(x+1)) for x in xrange(1,n+1)]:
        return True
    else:
        return False

def string_value(string,dict):       
    name = map(str.lower,[char for char in string.strip('""')])
    return sum([dict[char] for char in name])
        
if __name__ == "__main__":
    #build dictionary of alphabet values
    alphaValue = {}
    for idx, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
        alphaValue[char] = idx+1

    #verify test problem
    if isTriangle(string_value("SKY",alphaValue)):
        print "test passed."
    else:
        print "test failed!" 

    #read file and count triangle words
    word_list = open('words.txt','r').readline().split(',')

    result = len([word for word in word_list if isTriangle(string_value(word,alphaValue))])
        
    print "The answer to #42 is: %s" % result
