def pancake_flipper(S, K):
    """
    Returns the minimum number of K sign flips that are needed to have only 
    positive signs in the String. When one flip is performed, exactly K signs 
    must be flipped. Returns -1 if not possible.
    """
    if K > len(S):
        return 0
    counter = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            temp = S[i:i+K].replace('-', '#')
            temp = temp.replace('+', '-')
            temp = temp.replace('#', '+')
            S = S[:i] + temp + S[i+K:]
            counter +=1
    print("S after is {}".format(S))
    if '-' in S:
        return -1
    else:
        return counter

def main():
    s = "-+-+-"
    t = "---+-++-"
    u = "+++++"
    print(pancake_flipper(s,4))
    print(pancake_flipper(t,3))
    print(pancake_flipper(u,4))

if __name__ == "__main__":
    main()