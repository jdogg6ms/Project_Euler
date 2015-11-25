#!/usr/bin/env julia
# Project Euler Problem #3


# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

require("../modules/Primes.jl") 
import Primes
    
result = 1
num = 600851475143
sqrt_num = sqrt(num)+1

for i in 1:2:sqrt_num
    if num % i == 0
        factor = num / i
        if Primes.isPrime(i)
            result = maximum([i,result])
        end    
        if Primes.isPrime(factor)
            result = maximum([factor,result])
        end
    end
end

if result == 1
    result = num
end

println("The largest prime factor of $num is: $result")