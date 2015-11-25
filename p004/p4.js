#!/usr/bin/env nodejs
// Project Euler Problem #4
// find largest pallidrome as product of (2) 3-digit numbers

var nVals = 2;
var nDigits = 3;
var max_value = int('9'*nDigits)**nVals;
var done = false;

for (var i = max_value; i > 0 ; i-=1 ){

    if str(i) == str(i)[::-1]:
        for j in range(10**nDigits,1,-1):
            if i%j == 0 and j < 10**nDigits and i/j < 10**nDigits:
                print i,j, i/j
                result = i
                done = True
                break
    if (done == True)
        break;
}
console.log("The largest pallidrome of 2 3-digit numbers is: %s ", result)
