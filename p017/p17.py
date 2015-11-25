#!/usr/bin/env python
# Project Euler Problem #17
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
Ones = {'0':'',     '1':'one', '2':'two',   '3':'three', '4':'four', \
        '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

Tens = {'0':'',      '2':'twenty',  '3':'thirty', '4':'forty', '5':'fifty',\
        '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

Teens = {'10':'ten',      '11':'eleven',  '12':'twelve',  '13':'thirteen',\
         '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen',\
         '18':'eighteen', '19':'nineteen'}

def test_2digit(n):
    if int(n[-2]+n[-1]) in range(10,20):
        return Teens[n[-2]+n[-1]]
    else:
        return Tens[n[-2]] + Ones[n[-1]]

def string_value(n):
    n = str(n)
    output_string = ''
    if len(n) ==4:
        output_string += Ones[n[-4]]+'Thousand'
        n=n[1:]
    if len(n) ==3:
        if n[-3] != '0':
            output_string += Ones[n[-3]]+'Hundred'
        if n[-2] !='0' or n[-1] != '0':
            output_string+='And'
        n=n[1:]
    if len(n) ==2:
        output_string += test_2digit(n)
    if len(n) ==1:
        output_string = Ones[n[-1]]
    return output_string


if __name__ == "__main__":

    #verify test problem
    if len(string_value(342)) == 23 and len(string_value(115)) == 20:
        print "test passed."
    else:
        print "test failed!"

    result = sum([len(string_value(x)) for x in xrange(1,1000+1)])
    print "The answer to #17 is: %s" % result
