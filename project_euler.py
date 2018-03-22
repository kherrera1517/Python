from practice import isnum_palindrome
from prime import prime_factorization, is_prime
def multiples_of_3_5(n):
    """
    Gives a list of all numbers from 1 to n that are multiples of 3 and/or 5
    Input: integer
    Output: list of integers
    """
    return_list = []
    for i in range(1, n):
        if i%3 == 0 or i%5 == 0:
            return_list.append(i)
    # print(return_list)
    return return_list

def sum_fib(cap):
    if cap < 8:
        return 2

    fib1 = 1
    fib2 = 2
    temp = 0
    fibsum = 2

    while(temp < cap):
        temp = fib1 + fib2
        if temp%2 == 0:
            fibsum += temp
        
        fib1 = fib2
        fib2 = temp

    return fibsum

def largest_palindrome(num1, num2):
    """
    Finds the largest palindrome created by multiplying either the two given 
    integers together or any product of the numbers less than the initial two.
    """
    largest = 0
    for i in range(num1, 0, -1):
        for j in range(num2, 0, -1):
            if isnum_palindrome(i*j):
                if largest < i*j:
                    largest = i*j
    return largest

def smallest_divisible(n):
    """
    Finds the smallest positive number that is evenly divisible by all the
    numbers from 1 to n.
    """
    factors_list = []
    for i in range(1, n):
        ls = prime_factorization(i)
        for item in factors_list:
            if item in ls:
                ls.remove(item)
        factors_list.extend(ls)
    product = 1
    for x in factors_list:
        product *= x
    
    return product

def sum_square_difference(n):
    """
    Finds the difference between the sum of the squares of the first n natural
    numbers and the square of their sum.
    """
    sum1 = 0
    sum2 = 0
    for i in range(1, n+1):
        sum1 += i**2
        sum2 += i
    return sum2**2 - sum1

def nth_prime(n):
    i = 0
    j = 2
    prime = 2
    while(i<n):
        if is_prime(j):
            prime = j
            i += 1
        j += 1
    return prime

def largest_product_series(string, n):
    """
    Finds the n adjacent digits in the string that have the greatest product and
    returns that product.
    """
    largest_product = 0
    largest_product_subseries = ""
    for i in range(len(string)-n+1):
        temp_product = 1
        product_subseries = string[i:i+n]
        for j in range(n):
            temp_product *= int(product_subseries[j])
        if temp_product > largest_product:
            largest_product_subseries = product_subseries
            largest_product = temp_product
    print(largest_product_subseries)
    return largest_product

def special_pythagorean_triplet(num):
    """
    Finds the pythagorean triplet a, b, c that sums to the input integer.
    For m>n>0, a = m^2 - n^2, b = 2mn, c = m^2 + n^2.
    """
    m = 2
    while(True):
        for n in range(1,m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            k = 1
            while(True):
                a *= k
                b *= k
                c *= k
                triplesum = a+b+c
                if num == triplesum:
                    return (a, b, c)
                elif num > triplesum:
                    k += 1
                else:
                    break
        m += 1

def list_of_primes(ceiling):
    return_list = []
    for p in range(2,ceiling):
        if is_prime(p):
            return_list.append(p)

    return return_list


def main():
    # print(sum(multiples_of_3_5(1000)))
    # print(sum_fib(4000000))
    # print(largest_palindrome(999,999))
    # print(smallest_divisible(20))
    # print(smallest_divisible(20))
    # print(sum_square_difference(100))
    # print(nth_prime(10001))
    # s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    # print(largest_product_series(s,13))
    # print(special_pythagorean_triplet(1000))
    # print(sum(list_of_primes(2000000)))

if __name__ == "__main__":
    main()

