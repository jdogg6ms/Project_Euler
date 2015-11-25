#!/usr/bin/env lua

--[[
# Project Euler Problem #16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
--]]

function sumPower(num)
    str = tostring(num)
    local sum = 0
    for i = 1, #str do
        print (str, str:sub(i,i), sum)
        local c = str:sub(i,i)
        sum = sum + tonumber(c)
    end
    return sum
end

-- main --

if 26 == sumPower(2^15) then
    print ("Test passed.")
    result = sumPower(2^1000)
    print ("The sum of the digits of the number 2^1000: " .. result)
else
    print ("Test Failed! 26 != " .. sumPower(2^15))
end
