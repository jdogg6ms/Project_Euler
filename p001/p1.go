// Project Euler Problem #1

package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 1000; i++ {
		if i%3 == 0 || i%5 ==0 {
			sum += i
		}
	}
	fmt.Println("The sum of all natural numbers <1000 and divisible by 3 and 5 is:", sum)
}
