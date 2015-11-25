/*
*****************************************************************
*
*  a file of useful functions to be included in other programs
*
*****************************************************************
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>


bool isPrimeInt(int n){
	if (n < 2) {
		return false;
	}
	if (n == 2) {
		return true;
	}
	if (n % 2 ==0.0) { 
	    return false;
	}
    int x = 3;
	while (x < sqrt(n)+1) {
		if (n % x == 0) {
			return false;
		}
		x += 2;
	}
	return true;
}

