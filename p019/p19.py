#!/usr/bin/env python
# Project Euler Problem #19
"""
1 Jan 1900 was a Monday.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import date

def isMonday(input_date): 
    if input_date.weekday() == 0:
        return True

def isSunday(input_date): 
    if input_date.weekday() == 6:
        return True        
    
if __name__ == "__main__":

    #test
    if isMonday(date(1900,1,1)):
        print "Test #1 passed."
    else:
        print "Test #1 failed!"

    if isSunday(date(2012,4,29)):
        print "Test #2 passed."
    else:
        print "Test #2 failed!"  
    
    #find sundays that fell on first of the month
    sunday_count = 0
    for year in xrange(1901,2000+1):
        for month in xrange(1,12+1):
            if isSunday(date(year,month,1)):
                sunday_count +=1
   
    result = sunday_count

    print "The answer to #19 is: %s" %result 
