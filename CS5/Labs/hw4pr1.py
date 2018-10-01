# CS5 Gold/Black, hw4pr1
# Filename: hw4pr1.py
# Name: Kevin herrera 9/30/18
# Problem description: Binary <-> decimal conversions

def isOdd(N):
    return N%2==1

def numToBinary(N):
    if N == 0:
        return ''
    elif N%2 ==1:
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'

def binaryToNum(S):
    if S == '':
        return 0

    elif S[-1] == '1':
        return binaryToNum(S[:-1])*2 + 1
    else:
        return binaryToNum(S[:-1])*2 + 0

def increment(S):
    if S == '1'*8:
        return '0'*8
    else:
        num =  numToBinary(binaryToNum(S)+1)
        return '0'*(8-len(num))+num

def count(S, n):
    print(S)
    if n > 0:
        count(increment(S), n-1)
    else:
        return

def numToTernary(N):
    if N == 0:
        return ''
    elif N%3 == 1:
        return numToTernary(N//3) + '1'
    elif N%3 == 2:
        return numToTernary(N//3) + '2'
    else:
        return numToTernary(N//3) + '0'

def ternaryToNum(S):
    if S == '':
        return 0
    elif S[-1] == '1':
        return binaryToNum(S[:-1])*3 + 1
    elif S[-1] == '2':
        return binaryToNum(S[:-1])*3 + 2
    else:
        return binaryToNum(S[:-1])*3 + 0

def balancedTernaryToNum(S):
    if S == '':
        return 0
    elif S[-1] == '+':
        return balancedTernaryToNum(S[:-1])*3 + 1
    elif S[-1] == '-':
        return balancedTernaryToNum(S[:-1])*3 - 1
    else:
        return balancedTernaryToNum(S[:-1])*3 + 0

def numToBalancedTernary(N):
    if N == 0:
        return ''
    elif N%3 == 1:
        return numToBalancedTernary(N//3) + '+'
    elif N%3 == 2:
        return numToBalancedTernary((N+3)//3) + '-'
    else:
        return numToBalancedTernary(N//3) + '0'
