"""This module contains functions that deal with factorization algorithms."""

def factors(num):
    """
    Returns a unique sorted list of factors for the input integer.

    Input:
            n (integer): Number to find factors of.

    Output:
            returnlist (integer list): Unique list of all factors of the input.
    """

    returnlist = []

    if num < 3:   # Check the trivial cases first, 1 and 2
        for i in range(1, num+1):
            returnlist.append(i)
        return returnlist

    else:
        halfway = num//2

        for i in range(1, halfway+1):

            # Skip the work for things already existing in list. Stops repeats
            if i in returnlist:
                pass

            # Check for perfect squares to eliminate a root repeat
            elif i*i == num:
                returnlist.extend([i])

            else:
                if num%i == 0:
                    qint = num//i    # So number appears as integer in returnlist
                    returnlist.extend([qint, i])

        return sorted(returnlist)

def gcd_euclidean_alg(num1, num2):
    """
    Return the greatest common divisor of the two inputs using the Euclidean
    algorithm.

    Inputs:
            m (integer): Number to check against other for GCD.
            n (integer): Number to check against other for GCD.

    Outputs:
            (integer): The greatest common divisor. 1 if inputs are coprime.

    """

    if num1 == num2:
        return num1 # if the numbers are the same, their gcd is that number

    else:
        maxi = max(num1, num2)
        mini = min(num1, num2)
        diff = maxi - mini

        return gcd_euclidean_alg(diff, mini) # recruse through the algoirthm
