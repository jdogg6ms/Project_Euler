#!/usr/bin/env julia
# Project Euler Problem #9
"""
A Pythagorean triplet is a set of three natural numbers.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

function is_triplet(a,b,c) 
    return (a^2 + b^2 == c^2)
end

function calc_triplet(a,b) 
    return sqrt(a^2 + b^2)
end

done = false
for a in 1:1000
    for b in 1:1000
        c = calc_triplet(a,b)
        if a+b+c == 1000
            println("The triplet whose sum = 1000 is $(b), $(a), $(c), whose product is $(a*b*c) ")
            break
        elseif a+b+c >1000
            break
        end     
    end
end        