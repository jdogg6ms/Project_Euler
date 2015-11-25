#!/usr/bin/env lua

--[[
# Project Euler Problem #15

Starting in the top left corner of a 2 X 2 grid, there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20 X 20 grid?
--]]

-- defines a factorial function
function fact (n)
  if n == 0 then
    return 1
  else
    return n * fact(n-1)
  end
end

function solve_grid(nSquares)  --nCr permutation
    n = 2*nSquares
    r = nSquares
    return fact(n)/(fact(r)*(fact(n-r)))
end

-- main --

    --test
    if solve_grid(2) == 6 then
        print ("Test passed.")
    else
        print ("Test failed!")
    end

    result = solve_grid(20)

    print ("The answer to #15 is: " .. result)
