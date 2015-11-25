// Project Euler Problem #6
/*
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

package main

import( "fmt"

)  

func sumSquared(n int) int {
  sum := 0
  for i:= 1; i<=n ;i++ {  
    sum+= i*i    
  }
  return sum
}

func squareofSum(n int) int {
  sum := 0
  for i:=1;i<=n;i++ {  
    sum+= i    
  }
  return sum*sum
}

func main() {

  test :=10
  if squareofSum(test) - sumSquared(test) == 2640 {
    fmt.Println("Test case passed!")

    n := 100  
    delta := squareofSum(n) - sumSquared(n)   
    fmt.Println("The difference between squared sums and sum of squares is:", delta)
  
  }else {
  fmt.Println("The test case failed! 2640 !=", squareofSum(test),"-", sumSquared(test))
  }

  
  

}
