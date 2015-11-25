// Project Euler Problem #7
/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
*/

#include <stdio.h>
#include <math.h>
/*#include <stdbool.h>*/
#include"../modules/clib_fx.h"

int findPrimeCount(int nPrime) {
    int count = 1;
    int i;
    for (i = 3; count < nPrime; i+=2) {  
        if (isPrimeInt(i)){
          count+=1;
          if (count == nPrime) {
            break;
          }
        }   
    }
    return i;
}

int main() {

    int result = 0;
    if (findPrimeCount(6) == 13) {
        printf("Test case passed!\n");

        result = findPrimeCount(10001);
        printf("The 10,001st prime number is: %d\n", result);
  
    }else {
        printf("The test case failed! 13 != %d\n", findPrimeCount(6));
        
    }
    return 0;
}
