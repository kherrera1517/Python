# Add your Python code here. E.g.
from microbit import *

l = [(1,0),(1,1),(1,3),(1,4),(4,1)]

for x in range(5):
    for y in range(5):
        if (x,y) not in l and x != 3:
            display.set_pixel(x,y,5)