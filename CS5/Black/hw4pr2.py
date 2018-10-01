# CS5 Gold/Black, hw4pr2
# Filename: hw4pr2.py
# Name: Kevin Herrera 9/30/18
# Problem description:

def numToBase(N, B):
    if N == 0:
        return ''
    else:
        return numToBase(N//B,B) + str(N%B)

def baseBToNum(S, B):
    if S == '':
        return 0
    else:
        return baseBToNum(S[:-1], B)*B + int(S[-1])

def baseToBase(B1, B2, SinB1):
    num = baseBToNum(SinB1, B1)
    return numToBase(num, B2)

def add(S, T):
    snum = baseBToNum(S, 2)
    tnum = baseBToNum(T, 2)
    return numToBase(snum+tnum, 2)

# Helper Functions
def convertToNum(C):
    return numToBase(ord(C), 2)

def createNumList(S):
    return list(map(lambda x: convertToNum(x), S))

def xorStrings(S1, S2):
    return
