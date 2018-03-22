"""This module holds functions that use algorithms that deal with primality."""

from math import floor
from factoring import gcd_euclidean_alg

def is_prime(num):
    """
    Returns True if input number is prime by checking odd numbers up to the root
    of the input number and skipping any even numbers. Trial division method.

    Input: num (integer): Number to check primality of.

    Output: True if input is prime. False otherwise.

    """
    if (num == 2): # True is prime!
        return True
    elif (num == 1) or (num%2 == 0):
        return False          # 1 is not considered prime and we eliminate evens

    else:
        if num in [3, 5, 7]:    # Allows for loop below to start at 3, not 1ex
            return True

        else:
            root = num**.5

            if root%1 == 0:    # Checks for perfect squares
                return False

            else:               # We have an odd number to check primality of
                rootflr = floor(root)

                # Start at non-trivial potential factor (3) and skip over evens
                for i in range(3, rootflr+1, 2):

                    if num%i == 0:
                        return False # Not prime if integer divides p evenly

                    else:
                        pass    # Check the rest of the numbers for divisibility

    return True

def coprime(num1, num2):
    """
    Returns True if inputs are relatively prime to each other using the
    Euclidean algoirthm for greatest common divisor. If the greatest common
    divisor for the two input numbers is 1 then the numbers are coprime.

    Inputs:
            m (integer): Number to check against other for relative primality.
            n (integer): Number to check against other for relative primality.
    Outputs:
            True if inputs are realtively prime to each other. False otherwise.
    """

    if gcd_euclidean_alg(num1, num2) == 1:
        return True

    else:
        return False

def factorization_helper(num, ls):
    """
    Finds first prime factor of the input integer and adds it to the list of 
    prime factors. Recursively calls itself to complete the prime factorization 
    of the original input. If the original number is prime, it will return only
    that integer.
    """
    for i in range(floor(num**.5)+1):
        if is_prime(i) and num%i == 0:
            ls.append(i)
            return factorization_helper(num//i, ls)
    ls.append(num)
    return ls


def prime_factorization(num):
    """
    Wrapper function for the helper function that factors the input integer into
    prime factors.
    """
    return factorization_helper(num, [])

def unique_factorization_helper(num, ls):
    """
    Finds first prime factor of the input integer and adds it to the list of 
    prime factors. Recursively calls itself to complete the prime factorization 
    of the original input. Makes sure to not add factors that already exist.
     If the original number is prime, it will return only that integer.
    """
    for i in range(floor(num**.5)+1):
        if is_prime(i) and num%i == 0:
            if i not in ls:
                ls.append(i)
            return unique_factorization_helper(num//i, ls)
    if num not in ls:
        ls.append(num)
    return ls


def unique_prime_factorization(num):
    """
    Wrapper function for the helper function that factors the input integer into
    unique prime factors.
    """
    return unique_factorization_helper(num, [])

def main():
    print(prime_factorization(3**7))

if __name__ == "__main__":
    main()