#!/usr/bin/env nodejs
// Project Euler Problem #7
/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?

*/


function isPrime(n) {
    import math
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 ==0:
        return False
    else:
        x = 3
        while x < int(math.sqrt(n))+1:
            if n % x == 0:
                return False
            x+=2
        return True


def find_prime_count(nPrime):
    i = 3
    primes = [2]
    while len(primes) < nPrime:
        if isPrime(i):
            primes.append(i)
        i+=2
    return primes[-1]

if __name__ == "__main__":

    try: #verify alogrithm

        test = 6
        assert 13 == find_prime_count(test)
        print "Test case passed.\n"

        result = find_prime_count(10001)
        print "The 10,001st prime number is: %s" %(result)

    except:
      print "Test Case failed! %s != 13" %(find_prime_count(test))
      None
