#! /usr/bin/env nodejs
// Project Euler Problem #1

var sums = 0;
for (var i = 1; i < 1000; i++){
	if (i % 3 == 0 || i % 5 == 0){
		sums += i;
	}
}

console.log("The sum of all natural numbers <1000 and divisible by 3 or 5 is:", sums)
