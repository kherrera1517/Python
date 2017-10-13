from math import *
from factoring import *

def is_prime(p):
    """
    Returns True if input number is prime by checking odd numbers up to the root
    of the input number and skipping any even numbers. Trial division method.

    Input: n (integer): Number to check primality of.

    Output: True if input is prime. False otherwise.

    """
    if (p == 1) or (p%2 == 0):
        return False          # 1 is not considered prime and we eliminate evens

    else:
        if p in [3, 5, 7]:    # Allows for loop below to start at 3 instead of 1
            return True
        
        else:
            root = p**.5

            if root%1 == 0:    # Checks for perfect squares
                return False

            else:               # We have an odd number to check primality of
                rootflr = floor(root)
                
                # Start at non-trivial potential factor (3) and skip over evens
                for i in range(3, rootflr+1, 2):

                    if p%i == 0:
                        return False # Not prime if integer divides p evenly

                    else:
                        pass    # Check the rest of the numbers for divisibility

    return True

def coprime(m, n):
    """
    Returns True if inputs are relatively prime to each other using the 
    Euclidean algoirthm for greatest common divisor.

    Inputs:
            m (integer): Number to check against other for relative primality.
            n (integer): Number to check against other for relative primality.
    Outputs:
            True if inputs are realtively prime to each other. False otherwise.
    """
    if gcd_euclidean_alg(m, n) == 1:
        return True
    
    else:
        return False
