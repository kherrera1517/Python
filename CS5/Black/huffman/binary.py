def EightBitNumToBinary(num):
    output = ""
    while num > 0:
        output = str(num % 2) + output
        num = num // 2

    padding = 8 - len(output)
    return padding * "0" + output

def BinaryToNum(string):
    answer = 0
    for x in string:
        answer = answer * 2 + int(x)
    return answer
