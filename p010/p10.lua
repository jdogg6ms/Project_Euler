#!/usr/bin/env lua

--[[
Project Euler Problem #10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
]]

function isPrime(n)
    local prime = true

    if n < 2 then
        prime = false

    elseif n % 2 == 0 then
        prime = false

    else
        local x = 3
        limit = math.sqrt(n)+1
        while x < limit  do
            if n % x == 0 then
                prime = false
                break
            end
            x=x+2
        end
    end
    return prime
end

-- main --

sum = 2 -- first prime is 2

for i = 3, 2000000, 2 do
    if isPrime(i) then
        sum = sum + i
    end
end
print ("The sum of all primes under 2 million is " .. sum)

