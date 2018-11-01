import random
PUNCTUATION = [".", "!", "?"]

def dollarify(wordList, k):
    if wordList == [] or k == 0:
        return wordList
    returnList = []
    ind = 0 #keeps track of the beginning of a sentence
    for i in range(len(wordList)):
        if len(wordList[i]) != 1:
            returnList += ['$']*k + wordList[ind:i+1]
            ind = i+1
    return returnList

def markov_model(wordList, k):
    model = {}
    if wordList == [] or k == 0:
        return model
    else:
        dwList = dollarify(wordList, k)
        for i in range(len(dwList)-k):
            section = dwList[i:i+k]
            #We must make sure that the keys don't contain punctuations
            if True in map(lambda x: x[-1] in PUNCTUATION, section):
                continue
            else:
                key = tuple(section)
                if key not in model:
                    model[key] = []
                model[key] += [dwList[i+k]]
    return model

def gen_from_model(mmodel, numwords):
    if mmodel == {} or numwords == 0:
        return
    key_list = list(mmodel.keys())
    order = len(key_list[0])
    tempList = ['$']*order
    key = tuple(tempList)
    print_string = random.choice(mmodel[key])
    numwords -= 1
    while numwords > 0:
        print_string += ' '
        if print_string[-2] in PUNCTUATION:
            key = tuple(['$']*order)
            tempList += ['$']*order
        else:
            key = tuple(tempList[-order:])
        # print('key is now ', key)
        print_string += random.choice(mmodel[key])
        tempList += [print_string[-1]]
        numwords -= 1

    print(print_string)

def markov(fileName, k, length):
    return
