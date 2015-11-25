#!/usr/bin/env lua

--[[
Project Euler Problem #5
find smallest number that can be evenly divided by 1-20
]]


function testFactor(n)
    local num = n
    local result = true
    for i = 11, 19, 1 do
      if num % i ~= 0 then
        result = false
        break
      end
    end
    return result
end

-- Main Program --

i = 0
while true do
    i = i+20
    if testFactor(i) then
        break
    end
end

print ("The smallest number evenly divided by 1-20 is: " .. i)

