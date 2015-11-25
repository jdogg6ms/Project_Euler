/* Project Euler Problem #48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
*/

#include <stdio.h>
#include <math.h>

unsigned long long powInt(const unsigned long base, const unsigned long power){
    // a function to replace pow() and return an uint
    if (power == 1){
        return base;
    } else {
        return (base* powInt(base,power-1))%10000000000ul;
    }
}

unsigned long long last_ten(const unsigned x){
    // a fuction that returns the last ten digits of a sum of series x^x
    unsigned long long total = 0;
    unsigned long i;
    for (i = 1; i <= x; i++){
/*        printf("%llu, %llu\n", i, powInt(i,i)); //DEBUGG*/
        total +=(powInt(i,i));
    }
    return total % 10000000000ul;
}

int main() {

    if (last_ten(10) == 405071317){
        printf("Test passed.\n");

        printf("The answer to #48 is:%llu\n", last_ten(1000));

    } else {
        printf("Test failed! = %llu\n",last_ten(10));
    }
    return 0;                                 
}
