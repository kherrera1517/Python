#
# Field.py
#
# name: Kevin Herrera
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++
import random

class Field:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, deck_list, extradeck_list = []):
        """ the constructor for objects of type Date """
        self.deck = deck_list
        self.extra_deck = extradeck_list
        self.hand = []
        self.grave = []
        self.banish = []
        self.mzone = []
        self.stzone = []

    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        return str(self.deck)


    # here is an example of a "method" of the Date class:
    def shuffle(self):
        """ Shuffles the Deck. Should be changed to hand or deck!"""
        returnlist = []
        for i in range(len(self.deck)):
            card = random.choice(self.deck)
            self.deck.remove(card)
            returnlist.append(card)
        self.deck = returnlist

    def draw(self):
        """ Return top card of Deck. """
        self.hand.append(self.deck.pop(0))
        # return self.deck.pop(0)

    def add(self, cards):
        """ Search one card from Deck. """
        added = []
        for c in cards:
            if c in self.deck:
                added.append(c)
                self.deck.remove(c)

        if added == []:
            return None

        return added

    def return_to(self, cards):
        """ Returns cards to Deck.  SHOULD BE CHANGED TO GO FROM LOC TO DEST generic"""
        self.deck.extend(cards)

    def mill_top(self, dest = 'grave', amount = 1):
        for i in range(amount):
            if dest == 'grave':
                self.grave.append(self.deck.pop(0))
            else:
                self.banish.append(self.deck.pop(0))


def main():
    deck = ['Caspar', 'Caspar', 'Caspar', 'Starfire', 'Starfire', 'Starfire', 'Wild', 'Calamity', 
    'Kid', 'Kid', 'Dr', 'Dr', 'Ties of the Bretheren', 'Ties of the Bretheren', 'Ties of the Bretheren', 'Upstart Goblin',
    'Garnet', 'Garnet', 'Brilliant Fusion', 'Brilliant Fusion', 'One Day of Peace', 'Mind Control',
    'Ash Blossom', 'Ash Blossom', 'Pot of Desires', 'Pot of Desires', 'Double Summon', 'Magical Mallet',
    'Magical Mallet', 'Cross-Dominator', 'Cross-Dominator', 'Cross-Dominator', 'Death-perado', 
    'Death-perado', 'Death-perado', 'Dancing Needle', 'Devil\'s Deal', 'Deadman\'s Burst', 'Deadman\'s Burst', 'Deadman\'s Burst']
    # print(len(deck))
    f = Field(deck)
    f.shuffle()
    f.draw()
    f.draw()
    f.draw()
    f.draw()
    f.draw()
    print(f.hand)
    while(True):
        command = input("What would you like to do? ")
        if command == 'draw':
            f.draw()
        if command == 'mill':
            f.mill_top()
        if command  == 'banish':
            f.mill_top('banish')
        if command == 'quit':
            break
        print('Your hand is {}.'.format(f.hand))
        print('Your grave is {}.'.format(f.grave))
        print('Your banish is {}.'.format(f.banish))
    # print(d)
    # hand.append(d.draw())
    # hand.append(d.draw())
    # hand.append(d.draw())
    # hand.append(d.draw())
    # hand.append(d.draw())
    # print(d)
    # hand.extend(d.add( ['Starfire', 'Kid']))
    # print(d)
    # print(hand)

if __name__ == "__main__":
    main()
#
# be sure to add code for the Date class ABOVE -- inside the class definirun hw10pr1
#





#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#
    # another s.m. crash: Mondays in Oct. are risky...