# coding: utf-8
#
# the top line, above, is important -- 
# in ensures that Python will be able to use this file,
# even in the case you paste in text with unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
#
# Name:
#
#
import copy
import random

# function #1
#
def create_dictionary_dictionary(filename):
    """hi"""
    with open(filename) as f:
        worddict = {}
        words = []
        wordlist = []
        for line in f:
            wordlist += line.split()
        words += ["$"]
        for word in wordlist:
            words.append(word)
            if word[-1] in "!.?":
                words += ["$"]
        # print(words)

        for i in range(len(words)-1):
            # print(i)
            if words[i] in worddict:
                # print("comes in here! for {}".format(words[i]))
                innerdict = copy.copy(worddict[words[i]])

                if words[i+1] in innerdict:
                    innerdict[words[i+1]] += 1
                else:
                    # print("should come in here")
                    innerdict[words[i+1]] = 1
                    # print(innerdict)
                worddict[words[i]] = innerdict
            else:
                if words[i+1] == "$":
                    continue
                worddict[words[i]] = {words[i+1]:1}
        print(worddict)

def create_dictionary(filename):
    """create_dictionary"""
    with open(filename) as fname:
        worddict = {}
        words = []
        wordlist = []
        for line in fname:
            wordlist += line.split()
        words += ["$"]
        for word in wordlist:
            words.append(word)
            if word[-1] in "!.?":
                words += ["$"]
        print("The words list is {}.".format(words))

        for i in range(len(words)-1):
            if words[i] in worddict:
                if words[i][-1] in "!.?":
                    continue
                else:
                    worddict[words[i]].append(words[i+1])

            else:
                if words[i][-1] in "!.?":
                    continue
                else:
                    worddict[words[i]] = [words[i+1]]

        return worddict



# function #2
#
def generate_text(dictionary, num):
    """generate_text"""
    returnstring = ""
    lastword = " "
    for i in range(num):
        if i == 0 or lastword[-1] in '!.?':
            lastword = random.choice(dictionary['$'])
        else:
            lastword = random.choice(dictionary[lastword])
        returnstring += lastword + " "
    return returnstring[:-1]