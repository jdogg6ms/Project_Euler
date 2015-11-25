package main

import (
    "fmt"
//	"math"
)

//func isPrime(num float64) bool {
//	n := int(num)
//	if n < 2 {
//		return false
//	}
//	if n == 2 {
//		return true
//	}
//	if n % 2 ==0 { 
//	 return false
//	}
//	x := 3
//	limit := int(math.Sqrt(num))
//	for x <= limit {
//		if n % x == 0 {
//			return false
//		}
//		x += 2
//	}
//	return true
//}

func Factorial(x int) int {
    if x == 0 {
        return 1;
    } 
    return x * Factorial(x-1);
}


//func Factorial2(x int) int {
//   if x == 0 {
//      return 1	
//   } else {
//      return x * Factorial(x - 1)
//   }
//    return 0
//}

//func S(p int) int {      
//    for i:=1; i <=5; i++ { 
//        math.factorial(
//    
//    
//    }
//     
//    
//    return sum([factorial(p-k) for k in range(1,5+1)])%p


func main() {
    fmt.Println(Factorial(100000000))
}

//def S(p):      
//    return sum([factorial(p-k) for k in range(1,5+1)])%p
//        
//if __name__ == "__main__":
//    #verify test problem
//    if S(7) == 4:
//        print "test #1 passed."
//    else:
//        print "test failed!" 
//    
//    if sum([S(p) for p in range (5,100) if isPrime(p,primeSet, primeList)]) == 480:    
//        print "test #2 passed."
//    else:
//        print "test failed!"     
//        
//    result = sum([S(p) for p in xrange(5,100000000,2) if isPrime(p,primeSet, primeList)])  
//    print "The answer to #381 is: %s" %result 
