// Project Euler Problem #3
/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool isPrime(int n){
	if (n < 2) {
		return false;
	}
	if (n == 2) {
		return true;
	}
	if (n % 2 ==0.0) { 
	    return false;
	}
	if (n % 2 ==0.0) { 
	    return false;
	}
    int x = 3;
	while (x < sqrt(n)) {
		if (n % x == 0) {
			return false;
		}
		x += 2;
	}
	return true;
}

int primeFactors(long long num)
{
    int i;
    int result = 0;
    int factor = 0;
    
	for (i = 2; i < sqrt(num); i++){
	    if (num % i == 0) {
		    factor = num / i;
		    if (isPrime(i) && i > result) {
			    result = i;
		    }
		    if (isPrime(factor) && factor > result) {
			    result = factor;
            }
        }
    }    
    return result;
}

int main() {
    int result;
    const long long num = 600851475143;

    if (primeFactors(13195) == 29) {
        printf("Test passed.\n");
    } else { 
        printf("failed: %d\n",primeFactors(13195));    
    }

    result = primeFactors(num);

	printf("The largest prime factor of %lld is: %d \n", num, result);

    return 0;
}
