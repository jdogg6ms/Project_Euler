#!/usr/bin/env python
# Project Euler Problem #22

def string_value(string,dict,index):       
    name = map(str.lower,[char for char in string.strip('""')])
    return  index * sum([dict[char] for char in name])
        
if __name__ == "__main__":
    #build dictionary of alphabet values
    alphaValue = {}
    for idx, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
        alphaValue[char] = idx+1

    #verify test problem
    if string_value("COLIN",alphaValue,938) == 49714:
        print "test passed."
    else:
        print "test failed!" 

    #read file and sum values
    names_list = open('names.txt','r').readline().split(',')
    sum_names = 0

    for idx, item in enumerate(sorted(names_list)):
        sum_names+= string_value(item, alphaValue, idx+1)
    print "The sum of values of names in 'names.txt' is %s" %sum_names
