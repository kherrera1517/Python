"""
This script randomly decides which hero a user should pick in Overwatch based on
some requested inputs.
"""
from random import randint
from random import choice

#Author: Kevin Herrera
#RandomHero.py
#Date: 10/20/17

#List of all present Heroes as of 1/13/2017 
Heroes = {'Offense': ['Doomfist', 'Genji', 'McCree', 'Pharah', 'Reaper', 
                        'Soldier: 76', 'Sombra', 'Tracer'], 
          'Defense': ['Bastion', 'Hanzo', 'Junkrat', 'Mei', 'Torbjorn', 
                        'Widowmaker'],
          'Tank': ['D.Va', 'Orisa', 'Reinhardt', 'Roadhog', 'Winston', 'Zarya'],
          'Support': ['Ana', 'Lucio', 'Mercy', 'Symmetra', 'Zenyatta'],
          'DPS': [],
          'Healer': []}

#Fills DPS dictionary entry with all offensive heroes
for hero in Heroes['Offense']:
    Heroes['DPS'].append(hero)

#Fills DPS dictionary entry with all defensive heroes
for hero in Heroes['Defense']:
    Heroes['DPS'].append(hero)

#Fills Healer dictionary entry with all supports, excluding non-healers 
for hero in Heroes['Support']:
    if hero != 'Symmetra':
        Heroes['Healer'].append(hero)

#Used for the 'Anything' option when choosing hero for you
HeroClasses = ['Offense', 'Defense', 'Tank', 'Support'] 

possible_input = ['Offense', 'Defense', 'Tank', 'Support',
                  'DPS', 'Healer', 'Anything', 'Done']

def main():

    while True:
        heroType = input('What class of hero do you feel like playing today?\n'
                        'Your choices are Offense, Defense, Tank, Support, DPS,'
                        ' Healer, or Anything if you want me to pick.\n'
                        'If you are done, type Done.\n')

        #Makes sure user input is valid by checking it against possible_input
        while True:
            if heroType not in possible_input:
                heroType = input('That was not one of the possible choices.\n'
                                'Make sure you type Offense, Defense, Tank,'
                                ' Support, DPS, Healer, Anything if you want'
                                ' me to pick, or Done if you are done. Remember'
                                ' to capitalize!\n')

            else:
                break


        if heroType == 'Done':
            break
        
        elif heroType == 'Anything':
            heroType = choice(HeroClasses)
            randHero = randint(0,len(Heroes[heroType])-1)
        
        else:
            randHero = randint(0, len(Heroes[heroType])-1)
        hero = Heroes[heroType][randHero]    
        print("You should play {}!\n".format(hero))

#Calls main method when file is run
if __name__ == '__main__':
    main()