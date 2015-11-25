#!/usr/bin/env lua

--[[
Project Euler Problem #4
find largest pallidrome as product of (2) 3-digit numbers
--]]

function isPallindrome(num)
    if tostring(num) == string.reverse(tostring(num)) then
        return true
    end
end

-- Main Program --

local num = 999*999

while not result do
    if isPallindrome(num) then
        for j = 999,100,-1 do --3 digit factors
            if num % j ==0 and string.len(tostring(num/j)) == 3 then
                result = num
                break
            end
        end
    end
    num = num - 1
end

--result = 0
--for i = 999, 100, -1 do
--    for j = 999,100, -1 do --3 digit factors
--        local product = i*j
--        print (i, j, product)
--        if isPallindrome(product) then
--            if product > result then
--                result = product
--                break
--            else
--                break
--            end
--        end
--    end
--end

print ("The largest pallidrome of (2) 3-digit numbers is: " .. result)

