#!/usr/bin/env lua
--[[
The 12th term, F12, is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?
]]--

-- require"lbc"

function fibCount(n)
    local a = 1
    local b = 1
    local count = 2
    -- local count = bc.number(2)
    while string.len(tostring(b)) < n do
        a, b = b, a + b
        count = count +1
    end
    return count
end

assert(fibCount(3) == 12, "test case failed!")

-- requires arbitrary precision to solve for more that first 20 numbers
-- print("The first term in the Fibonacci sequence to contain 1000 digits is: ".. fibCount(1000))
