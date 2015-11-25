#!/usr/bin/env lua

--[[
Project Euler Problem #7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
--]]


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
    local i = 1
    local prime_count = 1
    while prime_count < nPrime do
        i = i + 2
        if isPrime(i) then
            prime_count = prime_count + 1
        end
    end
    return i, prime_count
end

---- Main Program --

local nPrimes = 10001

print("The 10,001st prime is: " .. find_prime_count(nPrimes))
