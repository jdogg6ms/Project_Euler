#!/usr/bin/env nodejs
// Project Euler Problem #3

/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
*/

var isPrime = function(n) {
    if (n < 2)
        return false;
    else if (n == 2)
        return true;
    else if (n % 2 ==0)
        return false;
    var x = 3;
    var limit = Math.sqrt(n)+1;
    while (x < limit){
        if (n % x == 0)
            return false;
        x+=2
    }
    return true
}

// tests
console.assert(isPrime(29), "29 failed isPrime()")
console.assert(!isPrime(486847), "486847 is not prime!")

var num = 600851475143;
var result = 1;

for (var i = Math.round(Math.sqrt(num))+1; i > 0; i-=2) {
    if (num % i == 0) {
        var factor = num / i;
        //console.log(i, factor, result);
        if (isPrime(i))
            result = Math.max(i, result);
        if (isPrime(factor))
            result = Math.max(factor, result);
    }
}

console.log("The largest prime factor of ", num, " is ", result)
