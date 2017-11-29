#
# Deck.py
#
# name:
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++
import random

class Deck:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, deck_list):
        """ the constructor for objects of type Date """
        self.deck = deck_list

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
        """ Shuffles the Deck. """
        returnlist = []
        for i in range(len(self.deck)):
            card = random.choice(self.deck)
            self.deck.remove(card)
            returnlist.append(card)
        self.deck = returnlist

    def draw(self):
        """ Return top card of Deck. """
        return self.deck.pop(0)

    def add(self, card, cards = None):
        """ Search one card from Deck. """
        if cards is None:
            if card in self.deck:
                self.deck.remove(card)
                return card
        else:
            added = []
            for c in cards:
                if c in self.deck:
                    added.append(c)
                    self.deck.remove(c)
            return added


    def return_to(self, cards, card = None):
        """ Returns cards to Deck. """
        if card is None:
            self.deck.extend(cards)
        else:
            self.deck.append(card)


def main():
    deck = ['Caspar', 'Caspar', 'Caspar', 'Starfire', 'Starfire', 'Starfire', 'Kid', 'Kid', 'Dr', 'Dr']
    d = Deck(deck)
    d.shuffle()
    print(d)
    d.draw()
    d.draw()
    print(d)
    d.add('', ['Starfire', 'Kid'])
    print(d)

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