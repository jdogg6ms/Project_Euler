// Project Euler Problem #2

package main

import "fmt"

func main() {
	sum := 0
	a := 1
	b := 1
	for a < 4000000 {
		a, b = b, a + b
		if a % 2 == 0 {
			sum += a
		}
	}
	fmt.Println("The sum of even values of fib sequence under 4 million is:", sum)
}
