#! /usr/bin/env lua
-- Project Euler Problem #2

sum = 0
a = 1
b = 1
repeat
    a, b = b, a + b
    if a % 2 == 0 then
        sum = sum + a 
    end
until a >= 4000000
print ("The sum of even values of fib sequence under 4 million is:" .. sum)

