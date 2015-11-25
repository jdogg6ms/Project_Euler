#include <stdio.h>

int main() {
    int sum = 0;
    int a = 1;
    int b = 1;
    int temp;
    while (a < 4E6){
    //a, b = b, a + b  fib sequence
        temp = a+b;
        a = b;
        b = temp;

        if (a % 2 == 0){
            sum += a; 
        }    
    }
    printf("The sum of even values of fib sequence under 4 million is:%d\n",sum);
    return 0;
}

