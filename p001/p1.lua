#! /usr/bin/env lua
-- Project Euler Problem #1

sum = 0

for i = 0, 1000-1 do
    if i%3 == 0 or i%5 == 0 then
    sum = sum + i
    end
end
print ('sum of all values below 1000 divisible by 3 or 5 is ' .. sum)   
