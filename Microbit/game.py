# Add your Python code here. E.g.
from microbit import *
from random import *

display.scroll("Left button is A, right button is B")
score = 0

while True:
    r = randrange(0,99)
    if r < 50:
        display.show(["A"])
        if button_a.is_pressed():
            score += 1
            continue
        elif button_b.is_pressed():
            break
        else:
            continue
    else:
        display.show(["B"])
        if button_b.is_pressed():
            score += 1 
            continue
        elif button_a.is_pressed():
            break
        else:
            continue
        
display.scroll("Your score is:")
display.show(str(score))