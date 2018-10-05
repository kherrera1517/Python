# Your name here
# Date
# hw4pr3.py

import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from functools import *

# A sample 8x8 image represented as a sequence of 64 bits
test1 = "0000001100001100000000110000001111111111111111111111111111111111"

def powerOfTwo(num):
    """ PROVIDED CODE. """
    """ Takes a positive integer as input and returns True if and only if it is a power of two. """
    if num == 1: return True
    elif num % 2 == 1: return False
    else: return powerOfTwo(num//2)

def pngToArray(filename, threshold=2):
    """ PROVIDED CODE. """
    """ Takes a filename as input, where the file is a .png image, and returns a binary
    2D array as output.  The image must be a square whose dimensions are a power of two. """
    img=mpimg.imread(filename)  # read in the image
    dimensions = img.shape  # Get the dimensions
    rows = dimensions[0]    # Extract the number of rows...
    columns = dimensions[1] # ... and columns
    if rows != columns or not powerOfTwo(rows):  # check if the image is of appropriate dimensions
        return None  
    array = []  # start building the output array
    for r in range(rows):
        row = []
        for c in range(columns):
            if sum(img[r][c]) >= threshold:
                row.append(0)
            else:
                row.append(1)
        array.append(row)
    return array

def renderASCII(array):
    """ PROVIDED CODE. """
    """ Takes a 2D array of 0's and 1's as input and renders it as 0's and 1's on the screen  """
    for row in array:
        stringify = reduce(lambda X, Y: str(X) + str(Y), row)
        print(stringify)
            
def renderImage(array):
    """ PROVIDED CODE. """
    """ Takes a 2D array of 0's and 1's as input and renders it on the screen using matplotlib. """
    dim = len(array)
    image = np.zeros((dim, dim), dtype = np.float)
    for r in range(dim):
        for c in range(dim):
            image[r][c] = float(array[r][c]) 
    plt.imshow(image, cmap="Greys", interpolation='nearest')
    plt.show()
    
def stringToArray(bstring):
    """ PROVIDED CODE. """
    """ Takes a binary string as input and returns the 2D array representation of the image. """
    dim = int(math.sqrt(len(bstring)))
    charArray = [list(bstring[i:i+dim]) for i in range(0, len(bstring), dim)]
    array = [ [int(x) for x in row] for row in charArray ]
    return array

def quadrants(array):
    """ Takes an array of bits as input and returns a list of quadrants
    of the form [NW, NE, SW, SE] where each entry is the array 
    for that quadrant """
    # You'll write this code!
    halfOuterArrLen = len(array)//2
    halfInnerArrLen = len(array[0])//2

    # NW = list(map(lambda x: array[x][:halfInnerArrLen], range(halfOuterArrLen)))
    # NE = list(map(lambda x: array[x][halfInnerArrLen:], range(halfOuterArrLen)))
    # SW = list(map(lambda x: array[x][:halfInnerArrLen], range(halfOuterArrLen, len(array))))
    # SE = list(map(lambda x: array[x][halfInnerArrLen:], range(halfOuterArrLen, len(array))))

    NW =[array[x][:halfInnerArrLen] for x in range(halfOuterArrLen)]
    NE =[array[x][halfInnerArrLen:] for x in range(halfOuterArrLen)]
    SW =[array[x][:halfInnerArrLen] for x in range(halfOuterArrLen, len(array))]
    SE =[array[x][halfInnerArrLen:] for x in range(halfOuterArrLen, len(array))]
    return [NW, NE, SW, SE]

def solidzero(array):
    """ Takes a 2D binary array as input and returns True if every bit is a 0 and False otherwise. """
    # You'll write this code.  One line suffices!
    # return max(list(map(lambda x: max(x), array))) == 0
    return max([max(x) for x in array]) == 0

def solidone(array):
    """ Takes a 2D binary array as input and returns True if every bit is a 1 and False otherwise. """
    # You'll write this code.  One line suffices!
    # return min(list(map(lambda x: min(x), array))) == 1
    return min([min(x) for x in array]) == 1

def makeQuadtree(array):
    """ Returns a quadtree representation of the array. """
    # You'll write this code
    if solidzero(array):
        return 0
    elif solidone(array):
        return 1
    else:
        # return list(map(lambda x: makeQuadtree(x), quadrants(array)))
        return [makeQuadtree(x) for x in quadrants(array)]

def solidArray(value, pixels):
    """ PROVIDED CODE. """
    """ Takes a value (0 or 1) and a number of pixels and retursn a 2D array of picelsxpixels
    bits all of which are set to the given value. """
    return [[value]*pixels for row in range(pixels)]

def makeArray(quadtree, dim):
    """ Takes a quadree and dimension as input and
    returns the 2D array representation of the quadtree """
    # You'll write this code
    return array

def rotateRight(quadtree):
    """ Takes a quadtuple as input and returns the quadtree that results when rotating that image
    clockwise 90 degrees. """
    # You'll write this code.  Around four lines of code suffice

def flipHorizontal(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping the image
    about the horizontal axis of symmetry. """
    # You'll write this code.  Around four lines of code suffice

def flipDiagonal(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping the image
    about the diagonal line through the NE and SW corners of the image. """
    # You'll write this code.  Around four lines of code suffice

def invert(quadtree):
    """ Takes a quadtree as input and returns the quadtree that results when flipping every white
    pixel to a black pixel and vice versa. """
    # You'll write this code.  Around four lines of code suffice
