#!/usr/bin/env julia
# Project Euler Problem #10
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

include("../modules/Primes.jl") 

prime_sum = sum([Primes.isPrime(i)? i :0 for i in 1:2000000])
         
println("The sum of all the primes below two million is: $prime_sum")