#!/usr/bin/env python
// Project Euler Problem #6
/*
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

function sums_squared(n){
  //Calculates the sum of squared of numbers from 1 to n
  var sum = 0;
  for (var i = 1; i <= n; i++){
    sum += Math.pow(i,2);
  }
  return sum;
}

function square_of_sums(n){
  // Calculates the squared sum of numbers from 1 to n
  var sum = 0;
  for (var i = 1; i <= n; i++){
    sum += i;
  }
  return Math.pow(sum, 2);
}

test = 10;
console.assert(2640 == square_of_sums(test)-sums_squared(test));
console.log("Test case passed.\n");

var n = 100;
var delta = square_of_sums(n) - sums_squared(n);
console.log("The difference between squared sums and sum of squares is: ", delta);
