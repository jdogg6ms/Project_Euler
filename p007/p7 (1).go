// Project Euler Problem #7
/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
*/

package main

import( "fmt"
        "math"
)  

func isPrime(n float64) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if math.Mod(n,2) ==0 { 
	 return false
	}
	x := 3.0
	for x < math.Sqrt((n))+1 {
		if math.Mod(n, x) == 0 {
			return false
		}
		x += 2
	}
	return true
}

func findPrimeCount(nPrime int) int {
    count := 1
    i:=1
    for ;count<=nPrime;i+=2 {  
        if isPrime(float64(i)){
            count+=1
            if count == nPrime {
                break
            }    
        }   
    }
    return i
}

func main() {

  test := 6
  if findPrimeCount(test) == 13 {
    fmt.Println("Test case passed!")

    result := findPrimeCount(10001)
    fmt.Println("The 10,001st prime number is:", result)
  
  }else {
  fmt.Println("The test case failed! 13 !=", findPrimeCount(test))
  }
}
