// Project Euler Problem #3

package main

import (
	"fmt"
	"math"
)

func isPrime(n float64) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if int(n) % 2 ==0 { 
	    return false
	}
	if math.Mod(n, 2) ==0 { 
	    return false
	}
	var x float64 = 3
	for x < math.Sqrt(n) {
		if math.Mod(n, x) == 0 {
			return false
		}
		x += 2
	}
	return true
}

func main() {
	var result float64 = 1
	var num float64 = 600851475143
	for i := 2.0; i < math.Sqrt(num); i++ {
		if math.Mod(num, i) == 0 {
			factor := num / i
			if isPrime(i) {
				if i > result {
					result = i
				}
			}
			if isPrime(factor) {
				if factor > result {
					result = factor
				}
			}
		}
	}
	fmt.Println("The largest prime factor of %f is: %f", num,result)
}
