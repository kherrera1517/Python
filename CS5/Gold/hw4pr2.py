# CS5 Gold/Black, hw4pr2
# Filename: hw4pr2.py
# Name: Kevin Herrera
# Problem description: Conversions and Compressions

#Function 1 numToBase(N,B)
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

def baseToBase(B1, B2, s_in_B1):
    num = baseBToNum(SinB1, B1)
    return numToBase(num, B2)

def add(S, T):
    snum = baseBToNum(S, 2)
    tnum = baseBToNum(T, 2)
    return numToBase(snum+tnum, 2)

def addB(S, T):
    if S == '':
        return T
    elif T == '':
        return S
    elif S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'
    elif S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    elif S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    else:
        return addB(S[:-1], addB(T[:-1], '1')) + '0'
