import math

"""
Function: trial_division, primality test through trial division method.
Inputs: p, number to check primality of.
Output: True if p is prime, False otherwise and prints pair of factors.

Checking primality of p with trial division by checking all integers m where m
is any integer from 2 to n. n is the square-root of p floored. We check only up
to n because if we think of the possible factors of a number p (excluding the
trivial 1 and p itself), they are the integers falling between 1 and p on the
natural number line 2, 3, 4.. p-2, p-1. n is the real number that, when
multiplied by itself, will give p; therefore, any integer greater than n-1 will
have already been accounted for by any number less than n. This is the case
because for any pair of integers (x ,y) that could possibly compose p, if y > r,
then it must be that case that x < r since x*y > r^2 if x > r and y > r AND
x*y < r^2 if x < r and y < r. Similarly, if y < r, then it must be the case that
x > r.
Take for example p = 24. The possible factors of p are 2 3 4 5 6 7 8 9 10 11
12 13 14 15 16 17 18 19 20 21 22 23. The root of p is r = 4.89897948557 and if
we floor it we get n = 4. We notice that 2 and 12, 3 and 8, and 4 and 6 are the
pairs of integers (x, y) that multiply to give us p. As x gets larger, y must
get smaller. Also, we only need to check up to n = 4 before we start seeing
integers that would have already been checked by integers less than r, such as
6 which was checked by 4 already.
The repition can be seen more clearly below for a perfect square (36):
2 * 18 = 3 * 12 = 4 * 9 = 6 * 6 = 9 * 4 = 12 * 3 = 18 * 2.
The repition begins after the root is reached.

Note: Large numbers may print wrong factors due to large floating point division
"""
def trial_division(p):
    if n <= 1:
        print("The definition of a prime number does not allow for negative numbers or 1") 
        return False
    #check if number is even
    if p%2 == 0:
        print("A pair of factors are", 2, "and", int(p/2))
        return False

    n = math.floor(p**.5)
    
    for i in range(2,n+1):
        if p%i == 0:
            print("A pair of factors are", i, "and", int(p/i))
            return False
    
    return True