# coding: utf-8
# name: Kevin Herrera 11/8/2018
# hw0pr2.py
#

import time          # includes a library named time
import random        # includes a library named random

choices = ['rock', 'paper', 'scissors']

# def valid_choice(weapon):
#     while weapon not in choices:
#             weapon = input('Please choose a valid weapon. D:< ')
#             weapon = weapon.lower()
#             print(name, '(you) chose', weapon)
    
#     return weapon


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
        print('Your weapons of choice are rock, paper or scissors!')
        your_weapon = input('Choose your weapon! It will not influence my choice, I promise. >:) ')
        your_weapon = your_weapon.lower()
        print(name, '(you) chose', your_weapon)
        
        while your_choice not in choices:
            your_choice = input('Please choose a valid weapon. D:< ')
            your_choice =your_ weapon.lower()
            print(name, '(you) chose', your_choice)

        bot_choice = random.choice(choices)
        print('By the way, I choose', bot_choice)

        if your_choice == 'rock':
            if bot_choice == 'rock':

        elif your_choice == 'paper':

        else:
            