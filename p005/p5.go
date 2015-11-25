// Project Euler Problem #5
//find smallest number that can be evenly divided by 1-20

package main

import (
	"fmt"
)

func testFactor(n int) bool {
	for i := 11; i < 21; i++ {
		if n%i != 0 {
			return false
		}
	}
	return true
}

func main() {
	result := 0
	for i := 0; result == 0; i += 20 {
		if testFactor(i) {
			result = i
		}
	}
	fmt.Println("The smallest number evenly divided by 1-20 is:", result)
}
