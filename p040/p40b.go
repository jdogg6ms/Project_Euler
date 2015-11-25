// Project Euler Problem #40
/*
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
*/

package main

import (
	"fmt"
	"math"
	"strconv"
)

func find_digit(n int) int {
	var s = string(n)
	var slen int
	index := 0
	for i := 1; ; i++ {
		s = strconv.Itoa(i)
		slen = len(s)
		index += slen
		if index >= n {
			break
		}
	}
	location := index - n
	if location == 0 {
		output, _ := strconv.Atoi(s[0:1])
		return output
	}
	//else
	output, _ := strconv.Atoi(s[(slen-(index-n))-1 : slen-(index-n)])
	return output
}

func main() {

	if find_digit(12) == 1 {
		fmt.Println("Test case passed.")

		result := 1
		for i := 0; i < 7; i++ {
			result *= find_digit(int(math.Pow(10, float64(i))))
		}
		fmt.Println("The answer to #40 is:", result)
	} else {
		fmt.Println("The test case failed!")
	}
}
