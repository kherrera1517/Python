from LinkedList import LinkedList
from hash_functions import hash1
#
# HashSet.py
#
# name: Kevin Herrera
#

import random

class HashSet:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, initial_size=10):
        """ the constructor for objects of type Date """
        self.size = 0
        self.buckets = initial_size
        self.reallocations = 0
        self.collisions = 0
        self.maximal = 0
        self.table = [None]*initial_size

    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        return str(self.table)

    def exists(self, value):
        """ 
        Checks if value exists in table.
        Input: Value to check
        Output: Boolean
        """
        hash_index = hash1(value)%self.buckets
        listatindex = self.table[hash_index]

        if listatindex is not None:


        return False


    # here is an example of a "method" of the Date class:
    def insert(self, value):
        """ Inserts value into table """


def main():


if __name__ == "__main__":
    main()