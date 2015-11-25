/* Project Euler Problem #5
 * find smallest number that can be evenly divided by 1-20
*/

#include <stdio.h>
#include <stdbool.h>

bool testFactor(int n) {
    int i;
	for (i = 11; i < 20; i++) {
        // all numbers are divisible by 1
        // since we are looping by factors of 20 we only need to test 11-19
		if (n%i != 0) {
			return false;
		}
	}
	return true;
}

int main() {
    int result = 0;
    int i;
	for (i = 0; result == 0; i += 20) {
		if (testFactor(i)) {
			result = i;
		}
	}
	printf("The smallest number evenly divided by 1-20 is: %d\n", result);
    return 0;
}
