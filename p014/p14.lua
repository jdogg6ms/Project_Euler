#!/usr/bin/env lua

--[[
Project Euler Problem #14

The following iterative sequence is defined for the set of positive integers:

n =  n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
--]]


function series(n, Dict)
    i = n
    length = 1
    while i > 1 do
        if Dict[i] then
            length = Dict[i] +length
            break
        else
            if i % 2 ==0 then
                i = i/2
            else
                i = 3*i +1
            end
            length = length +1
        end
    end
    Dict[n] = length
    return length
end

-- main --

    valuesDict = {}
    result = 1

    if series(13,valuesDict) == 10 then
        print ("Test passed.\n")
    else
        print ("Test failed!", series(13,valuesDict))
    end

    max_length = 0
    for i = 1, 999999, 1 do
        length = series(i, valuesDict)
        if length > max_length then
            max_length = length
            result = i
        end
    end
    print("The answer to #14 is " .. result)
