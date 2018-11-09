# coding: utf-8
# name: Kevin Herrera 11/8/2018
# hw0pr2a.py
#

import time          # includes a library named time
import random        # includes a library named random

choices = ['rock', 'paper', 'scissors']

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game ...)
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    name = input('Hi...what is your name? ')
    print()
    print("Hmmm...")
    print()

    # We start off with some special cases for fun!
    if name == 'Eliot' or name == 'Ran':
        print('I\'m "offline" Try later.')
    
    elif name == 'Zach':
        print('Do you mean Jeff?')
        time.sleep(2)
        print('No?')
        time.sleep(1)
        print('Oh.')
        
    else:
        print('Welcome,', name)
        time.sleep(2)
        print('Your weapons of choice are rock, paper or scissors!')
        time.sleep(2)
        your_choice = input('Choose your weapon! It will not influence my choice, I promise. >:) ')
        your_choice = your_choice.lower()
        print(name, '(you) chose', your_choice)
        time.sleep(2)
        
        bot_choice = random.choice(choices)
        print('By the way, I choose', bot_choice)
        time.sleep(2)

        if your_choice == 'rock':
            if bot_choice == 'rock':
                print("A tie?! Let's go again!")

            elif bot_choice == 'paper':
                print("Ha! I win. >:P")

            else:
                print("That was a fluke. Rematch me!")

        elif your_choice == 'paper':
            if bot_choice == 'paper':
                print("A tie?! Let's go again!")

            elif bot_choice == 'scissors':
                print("Ha! I win. >:P")

            else:
                print("That was a fluke. Rematch me!")

        elif your_choice == 'scissors':
            if bot_choice == 'scissors':
                print("A tie?! Let's go again!")

            elif bot_choice == 'rock':
                print("Ha! I win. >:P")

            else:
                print("That was a fluke. Rematch me!")

        else:
            print("That's not a valid choice! Try again next time!")