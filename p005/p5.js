#!/usr/bin/env python
//Project Euler Problem #5
 //find smallest number that can be evenly divided by 1-20

function test_factor(n){
  for (var i = 11; i <= 20; i++){
    if (n % i !=0)
      return false;
  }
  return true;
}

var i = 0;
var result = 0;
while (result == 0) {
    i +=20;
    if (test_factor(i))
        result = i;
}
console.log("The smallest number evenly divided by 1-20 is: ", result)
