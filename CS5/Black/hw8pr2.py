import random
PUNCTUATION = [".", "!", "?"]

def dollarify(wordList, k):
    if wordList == [] or k == 0:
        return wordList
    returnList = []
    ind = 0 #keeps track of the beginning of a sentence
    for i in range(len(wordList)):
        if wordList[i][-1] in PUNCTUATION:
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

    # print(mmodel)
    key_list = list(mmodel.keys())
    order = len(key_list[0])
    tempList = ['$']*order
    key = tuple(tempList)
    tempList += [random.choice(mmodel[key])]
    print_string = str(tempList[-1])
    numwords -= 1

    while numwords > 0:
        print_string += ' '
        if print_string[-2] in PUNCTUATION:
            key = tuple(['$']*order)
            tempList += ['$']*order
        else:
            key = tuple(tempList[-order:])
        print('key is now ', key)
        tempList += [random.choice(mmodel[key])]
        print_string += tempList[-1]
        numwords -= 1
        print(print_string)
        print(tempList)

    print(print_string)

def markov(fileName, k, length):
    file1 = open(fileName)
    inputList = file1.readlines()
    file1.close()
    cleanList = list(map(lambda x: x.replace("\n", " "), inputList))
    # print(cleanList)
    cleanString = "".join(cleanList)
    finalList = cleanString.split()
    # print(finalList)
    model = markov_model(finalList, k)
    # print(model.keys())
    gen_from_model(model, length)
