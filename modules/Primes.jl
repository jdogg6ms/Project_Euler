#!/usr/bin/env julia
# Prime testing 

module Primes
export isPrime

function isPrime(n) ## brute force
    if n < 2
        return false
    elseif n == 2 
        return true
    elseif n % 2 == 0
        return false
    else 
        x = 3
        limit = sqrt(n)+1    
        while x <= limit
            if n % x == 0
                return false
            end
            x+=2
        end
        return true  
    end
end
"""
function gen_primes(max_n)
    #sundaram
    numbers = 3:2:max_n+1
    half = (max_n)//2
    initial = 4

    for step in 3:2:max_n+1
        for i in initial:half:step
            numbers[i-1] = 0
        end
        initial += 2*(step+1)

        if initial > half
            return [2] + filter(None, numbers)
        end
    end
end
"""
end
