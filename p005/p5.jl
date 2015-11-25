#!/usr/bin/env julia
# Project Euler Problem #5
# find smallest number that can be evenly divided by 1-20

function test_factor(n)
  for i in 11:20
    if n % i !=0
      return false
    end
  end  
  return true
end

i = 0
result = 0
while result == 0
    i+=20
    if test_factor(i)
        result = i
    end
end
    println ("The smallest number evenly divided by 1-20 is: $(result)")