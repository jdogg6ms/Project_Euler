#!/usr/bin/env nodejs
//Project Euler Problem #2

var sum = 0;
var a = 1;
var b = 1;

while (a < 4000000){
	// console.log(a, sum)
	var c = a + b
	a = b;
	b = c;
    if (a % 2 == 0){
        sum += a
    }
}

console.log("The sum of even values of fib sequence under 4 million is: ", sum)

