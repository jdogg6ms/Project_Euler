#! /usr/bin/env julia
# Project Euler Problem #1

sum = 0

for i in 3:1000-1
	if i % 3 == 0 || i % 5 == 0
		sum += i
	end	
end	

println("The sum of all natural numbers <1000 and divisible by 3 or 5 is: $(sum)")