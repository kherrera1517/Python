from functools import reduce

def getInput():
    userInput =   input("Enter some words: ")
    print(userInput)  # prints the userInput string
    print(userInput.split())  # splits the userInput into a list of strings and prints that list

miniWordList = ["a", "am", "amp", "ample", "as", "asp", "at", "ate", "sat",
                "spa", "spam", "tea", "was", "wasp"]

# def wordBreak(string):
#     scoreFunction = len  # We're setting the scoring function.  We can change that function to something else!
#     wordList = miniWordList  # We're setting the list of valid words.  It can be changed to something else!
#     userInput = input("Enter your best solution: ")  # Get user input                                   
#     userList = userInput.split() # split the input string into a list of strings                        
#     if check(userList, string, wordList):
#         userScore = reduce(lambda X, Y: X+Y, map(scoreFunction, userList))
#         print("Your score was ", userScore)
#         best = showStringScore(string, scoreFunction, wordList, {})
#         print("Best solution is ", best)
#     else:
#         print("Your solution wasn't valid!")

def check(playerList, string, wordList):
    if playerList == []:
        return True
    elif string == "":
        return False
    elif playerList[0] in wordList and playerList[0] in string:
        index = string.index(playerList[0]) + len(playerList[0])
        return check(playerList[1:], string[index:], wordList)
    else:
        return False

def stringScore(string, scoreFunction, wordlist, memo):
    if string == "":
        return 0
    elif string in memo:
        return memo[string]
    else:
        loseIt = stringScore(string[1:], scoreFunction, wordlist, memo)
        useitIndices = list(filter(lambda x: string[:x+1] in wordlist, range(len(string))))
        useIt = list(map(lambda x: scoreFunction(string[:x+1]) + 
        stringScore(string[x+1:], scoreFunction, wordlist, memo), useitIndices))
        finalList = useIt + [loseIt]
        final = max(finalList)
        memo[string] = final
        return final

def showStringScore(string, scoreFunction, wordlist, memo):
    if string == "":
        return [0,[]]
    elif string in memo:
        return memo[string]
    else:
        loseIt = showStringScore(string[1:], scoreFunction, wordlist, memo)
        useitIndices = list(filter(lambda x: string[:x+1] in wordlist, range(len(string))))
        useitDetails = list(map(lambda x: [scoreFunction(string[:x+1]), string[:x+1], showStringScore(string[x+1:], scoreFunction, wordlist, memo)], useitIndices))
        useIt = list(map(lambda x: [x[0]+x[2][0], [x[1]]+x[2][1]], useitDetails))
        finalList = useIt + [loseIt]
        final = max(finalList)
        memo[string] = final
        return final

# def test(count, memo):
#     if count == 0:
#         return
#     else:
#         print("len of memo1 is", len(memo))
#         print(memo)
#         memo[count] = count
#         test(count-1, memo)
#         print("len of memo2 is", len(memo))
#         print(memo)
