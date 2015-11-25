// Project Euler Problem #4
// find largest pallidrome as product of (2) 3-digit numbers

#include <stdio.h>
#include <strings.h>
#include <math.h>

const char * StrReverse(char s[])
{
    int length = strlen(s) ;
    int i, j;
    char str[length]

    for (i = 0, j = length - 1; i < j; i++, j--)
     {
         str[j] = s[i];
      }
    return str
}

bool isPallidrome(int n){
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



int main(){

    int max_value = 999*999;
    int i = 0;
    int j = 0;
    int result = 0;

    for (i = max_value; result ==0 ; i--){
        if (isPallidrome(i)){
            for (j = 999; j--){
                if (i % j ==0) && (i/j )

                }
            }

        }
/*            for j in range(10**nDigits,1,-1):
                if i%j == 0 and j < 10**nDigits and i/j < 10**nDigits:
                    print i,j, i/j
                    result = i
                    done = True
                    break
        if done == True:
          break
    }

    //print "The largest pallidrome of (%s) %s-digit numbers  is: %s" %(nVals, nDigits, result)
}
