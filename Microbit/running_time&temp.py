# Add your Python code here. E.g.
from microbit import *

while True:
    display.scroll("Running time is:")
    display.scroll(str(running_time()))
    display.scroll("Temp. is:")
    display.scroll(str(temperature()))
