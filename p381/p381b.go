// Project Euler Problem #381
/*
For a prime p let S(p) = ((p-k)!) mod(p) for 1 <= k <= 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.
It can be verified that Sum(S(p)) = 480 for 5 <= p < 100.
Find Sum(S(p)) for 5 <=  p < 10^8.
*/

package main

import (
    "fmt"
	"math"
    "math/big"
)

func isPrime(n int) bool {
	num := float64(n)
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n % 2 ==0 { 
	 return false
	}
	x := 3
	limit := int(math.Sqrt(num))
	for x <= limit {
		if n % x == 0 {
			return false
		}
		x += 2
	}
	return true
}

func Factorial(x float64) float64 {
    if x == 0 {
        return 1;
    } 
    return x * Factorial(x-1);
}

func S(p float64) float64 {  
    var sum float64 = 0
    var k float64    
    for k = 1; k <6; k++ { 
//        fmt.Println(p,k,p-k,Factorial(p-k))
        sum += Factorial(p-k)
    }
    return math.Mod(sum,p)
}

func SumOfS(i,j float64) float64 {
    var sum float64 = 0
    for p:=i; p < j; p++ {
        if isPrime(int(p)) {
//            fmt.Println(p, S(p))
            sum+= S(p)
        }
    }
    return sum  
}

func main() {
    if S(7) == 4 {
        fmt.Println("Test #1 passed.")
    } else {
        fmt.Println("Test #1 failed!")
    }  
   

    if SumOfS(5,100) == 480 {
        fmt.Println("Test #2 passed.")
    } else {
        fmt.Println("Test #2 failed!", SumOfS(5,100) )
    }        
}
//        
//    result = sum([S(p) for p in xrange(5,100000000,2) if isPrime(p,primeSet, primeList)])  
//    prfloat64 "The answer to #381 is: %s" %result 
