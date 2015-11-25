#!/usr/bin/env lua

--[[
Project Euler Problem #9

A Pythagorean triplet is a set of three natural numbers.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
--]]

function isTriplet (a, b, c)
    if a^2 + b^2 == c^2 then
        return true
    end
end

function calcTriplet(a, b)
    return math.sqrt(a^2 + b^2)
end

-- main --

for a = 1, 1000, 1 do
    for b = 1, 1000, 1 do
        c = calcTriplet(a, b)
        local sum = a + b + c
        if sum == 1000 then
            product = a*b*c
            print("Triples = " .. a  ..  ", " .. b .. ", " .. c)
            done = true
        elseif sum > 1000 then
            break
        end
    end
    if done then
        break
    end
end
print("product = " .. product)

--alternate: ((slower than above)
--find c by 1000 - a -b and then check triplet

--for a = 1, 1000, 1 do
--    for b = 1, 1000, 1 do
--        local c = 1000 - a - b
--        if isTriplet(a,b,c) then
--            product = a*b*c
--            print("Triples = " .. a  ..  ", " .. b .. ", " .. c)
--            done = true
--        end
--    end
--    if done then
--        break
--    end
--end
--print("product = " .. product)

