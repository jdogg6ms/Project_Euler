// Project Euler Problem #4
// find largest pallidrome as product of (2) 3-digit numbers

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
	if isPrime(num) {
		result = num
	} else {

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
	}
	fmt.Println("The largest pallidrome as product of (2) 3-digit numbers", num, "is:", result)
}

/*
    nVals = 2
    nDigits = 3
    max_value = int('9'*nDigits)**nVals
    done = False

    for i in range(max_value,1,-1):
        if str(i) == str(i)[::-1]:
            for j in range(10**nDigits,1,-1):   
                if i%j == 0 and j < 10**nDigits and i/j < 10**nDigits:
                    print i,j, i/j    
                    result = i
                    done = True
                    break
        if done == True: 
          break            
    print "The largest pallidrome of (%s) %s-digit numbers  is: %s" %(nVals, nDigits, result)
*/
