import random
import math


def is_pandigital(x):
    num = str(x)
    dict = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    if len(num)>10:
        return False
    for i in num:
        dict[i]+=1
        if dict[i]>1:
            return False
    return True



def gen_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

# Python3 program Miller-Rabin primality test

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
    # Initialize result
    res = 1;

    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):

        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;

            # y must be even now
        y = y >> 1;  # y = y/2
        x = (x * x) % p;

    return res;


# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);

    # Compute a^d % n
    x = power(a, d, n);

    if (x == 1 or x == n - 1):
        return True;

        # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

            # Return composite
    return False;


# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def is_prime(n):
    # Corner cases
    k=4
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

        # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;

        # Iterate given nber of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;

    return True;

def is_palindrome(x):
    x = str(x)
    if len(x)%2 ==0:
        i = int(len(x)/2)
        t = i+1
    else:
        i = t = int(math.ceil(len(x)/2))

    lret = True
    while i>0:
        if x[i-1]==x[t-1]:
            i-=1
            t+=1
        else:
            lret = False
            break

    return lret