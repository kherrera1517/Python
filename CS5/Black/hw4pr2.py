# CS5 Gold/Black, hw4pr2
# Filename: hw4pr2.py
# Name: Kevin Herrera 9/30/18
# Problem description:
from functools import reduce
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
def createOrdList(string):
    # return list(map(lambda x: ord(x), string))
    return [ord(c) for c in string]

def mapXor(numList1, numList2):
    return list(map(lambda x,y: x^y, numList1, numList2))

#Below are the helper functions used in our final implementation of xorStrings
def createBList(string):
    # return list(map(lambda x: numToBase(ord(x), 2), string))
    return [numToBase(ord(c), 2) for c in string]

def create8BList(bitList):
    # return list(map(lambda x: '0'*(8-len(x))+x, bitList))
    return ['0'*(8-len(l))+l for l in bitList]

def createNumList(bitList):
    # return list(map(lambda x: baseBToNum(x, 2), bitList))
    return [baseBToNum(b, 2) for b in bitList]

def xOr(bit1, bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"

def xorStrings(S1, S2):
    bitList1 = createBList(S1)
    bitList2 = createBList(S2)
    
    eightBitL1 = create8BList(bitList1)
    eightBitL2 = create8BList(bitList2)

    xOrList = list(map(lambda x, y: reduce(lambda m, n: m+n, list(map(lambda s, t: xOr(s, t), x, y))) , eightBitL1, eightBitL2))
    numList = createNumList(xOrList)
    
    return reduce(lambda x, y: x+y, list(map(lambda z: chr(z), numList)))

def newXorStrings(string1, string2):
    numList1 = createOrdList(string1)
    numList2 = createOrdList(string2)

    finalNumList = mapXor(numList1, numList2)

    return reduce(lambda x, y: x+y, list(map(lambda z: chr(z), finalNumList)))

# ^ is xor