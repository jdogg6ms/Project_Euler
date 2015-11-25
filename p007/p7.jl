#!/usr/bin/env julia
# Project Euler Problem #7
"""
By listing the first six prime numbers 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?

"""
require("../modules/Primes.jl") 
import Primes

function find_prime_count(nPrime)
    i = 3
    primes = [2]
    while length(primes) < nPrime
        if Primes.isPrime(i)
            push!(primes,i)
        end
        i+=2
    end
    return primes[length(primes)]
end

@assert 13 == find_prime_count(6)
result = find_prime_count(10001)
println("The 10,001st prime number is $(result)") 