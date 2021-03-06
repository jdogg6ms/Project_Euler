/*
# Project Euler Problem #12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
*/

package main

import( "fmt"
        "math"
)

func divisors(num uint) uint {
    var count, x, limit uint = 0, 0, uint(math.Sqrt(float64(num)+1))
	if num % 2 == 0 {
	    for x=1; x < limit; x+=1 {
		    if num % x == 0 {
			    count += 2
		    }
	    }
    }else {
        for x=1; x < limit; x+=2 {
		    if num % x == 0 {
			    count += 2
		    }
	    }
	}
	return count
}
   
  
func main() {
    //test
    if divisors(28) > 5 {
        fmt.Println("Test #1 passed.")
    }else{
        fmt.Println("Test #1 failed!", divisors(28))
    }    

    //find first triangle number to have over five hundred divisors 
    var triangle, count uint = 0, 0
    for count=0; divisors(triangle) < 500; count+=1 {
        triangle += count 
    }   
    fmt.Println("The answer to #12 is:", triangle) 
}
