def factor(n):
    """
    Returns a unique sorted list of factors for the input integer.

    Input:
            n (integer): Number to find factors of.
    
    Output:
            returnlist (integer list): Unique list of all factors of the input.
    """

    returnlist = []

    if n < 3:   # Check the trivial cases first, 1 and 2
        for i in range(1, n+1):
            returnlist.append(i)
        return returnlist
    
    else:
        quotient = n//2

        for i in range(1, quotient+1):

            # Skip the work for things already existing in list. Stops repeats
            if i in returnlist:
                pass

            # Check for perfect squares to eliminate a root repeat
            elif i*i == n:
                returnlist.extend([i])
                
            else:
                q = n/i

                if q%1 == 0:
                    qint = n//i    # So number appears as integer in returnlist
                    returnlist.extend([qint, i])
                    
        return sorted(returnlist)

def gcd_euclidean_alg(m, n):
    """
    Return the greatest common divisor of the two inputs using the Euclidean 
    algorithm.

    Inputs:
            m (integer): Number to check against other for GCD.
            n (integer): Number to check against other for GCD.
    
    Outputs:
            (integer): The greatest common divisor. 1 if inputs are coprime.

    """

    if m == n:
        return m # if the numbers are the same, their gcd is that number

    else:
        maxi = max(m, n)
        mini = min(m, n)
        diff = maxi - mini

        return gcd_euclidean_alg(diff, mini) # recruse through the algoirthm
