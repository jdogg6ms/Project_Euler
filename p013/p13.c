/*
# Project Euler Problem #13
"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
Read in file "input.txt"
"""
*/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <math.h>

/***********************************************************************
    sumArray() assumes array[0] is the "ones" place and is indexed to the right
    ex: value 123
    3 = array[0]
    2 = array[1]
    1 = array[2]
 ***********************************************************************
*/

void sumArray(int *sumArray_ptr,    // sum of sumArray += inputArray
             int *inputArray_ptr,   // array to add to sum
             int in_size)           // length of array to add to sum
             {
    int i;
    int total;
    for (i=0; i<in_size; ++i) { 
        total = *inputArray_ptr + *sumArray_ptr;
        if (total >= 10) {
            *sumArray_ptr = total % 10;
            *(++sumArray_ptr) +=1; // carry the one to the next digit
            sumArray_ptr-=1;       // move pointer back to previous loc.
        } else {
            *sumArray_ptr = total;
        }
        ++ inputArray_ptr;
        ++ sumArray_ptr;
    }
}

int main() {

    FILE    *fp;
    int     sums[80]        = {0};  // sum of each line
    int     inArray[52]     = {0};  // array of ints of read line
    char    line[52]        = {0};  // array of char values from file line

    fp = fopen("input.txt","r");
    if (fp == NULL){
        printf("Error opening file");
        return 1;                   // Exit on Error
    }

    /*reads one line of file, stops at EOF*/    
    while(fgets(line, sizeof(line), fp) != NULL) {
    

        /* reverse array and convert each line into array of integers*/
        for (int i = 0; i < 50; i++) {  
            sscanf(&line[i], "%1d", &inArray[49-i]);
        }
        
        /* pass each array from file line to function to sum with sums*/
        sumArray(sums, inArray, sizeof(inArray)/sizeof(*inArray));    
    }
    fclose(fp);
    

    /* print the last/first ten digits of sum*/    
    printf("the answer is: ");
    int loc = 80 -1; // index of sums array, start at last element

    /* skip leading zeros in sums array*/
    while (sums[loc] == 0) {
        --loc;
    }    
    
    /* print first ten digits of sum */
    for (int i = 0; i <10; ++i) {
        printf("%d", sums[loc]);
        --loc; 
    }
    printf("\n");
    return 0;
}
