#!/usr/bin/env lua

--[[
Project Euler Problem #6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.  Find the difference
between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
--]]


function sum_of_squares(n)
    local sum = 0
    for i = 1, n, 1 do
        sum = sum + i^2
        end
    return sum
end

function square_of_sums(n)
    local sum = 0
    for i = 1, n, 1 do
        sum = sum + i
        end
    return sum^2
end


-- Main program --

nat_nums = 1000

-- test functions
if sum_of_squares(10) ~= 385 then
    print("test1 failed")

elseif square_of_sums(10) ~= 3025 then
    print("test2 failed")

else -- run program if test passed
    local result = square_of_sums(nat_nums) - sum_of_squares(nat_nums)
    print (
    [[The difference between the sum of the squares of the first one-hundred
natural numbers and the square of the sum is ]] .. result)
end
