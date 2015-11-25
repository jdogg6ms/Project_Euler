#!/usr/bin/env julia
# Project Euler Problem #6
"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

function sums_squared(n)
  """ Calculates the sum of squared of numbers from 1 to n"""
  return sum([x^2 for x in 1:n])
end

function square_of_sums(n)
  """ Calculates the squared sum of numbers from 1 to n """
  return sum([x for x in 1:n])^2
end

#test case
@assert (3025 - 385) == (square_of_sums(10)-sums_squared(10))
#println ("$(square_of_sums(10))")
#println ("$(sums_squared(10))")

n = 100
delta = square_of_sums(n) - sums_squared(n)
println("The difference between squared sums and sum of squares is $(delta)")