#!/usr/bin/env lua

--[[
Project Euler Problem #3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
]]


function isPrime(n)
    local prime = true

    if n < 2 then
        prime = false

    elseif n == 2 then
        prime = true

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

function find_prime_count(nPrime)
    local i = 3
    prime_count = 1
    while prime_count < nPrime do
        if isPrime(i) then
            prime_count = prime_count + 1
        end
        i = i + 2
    end
    return prime_count, i
end



-- Main Program

num = 600851475143
result = 1

for i = 3, math.sqrt(num)+1, 2 do
    if num % i == 0 then
        factor = num / i
        if isPrime(i) then
            if i > result then
                result = i
            end
        end
        if isPrime(factor) then
            if factor > result then
                result = factor
            end
        end
    end
end

print ("The largest prime factor of 600851475143 is: " .. result)

