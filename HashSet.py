from LinkedList import *
from hash_functions import hash1
#
# HashSet.py
#
# name: Kevin Herrera
#

import random

class HashSet:
    """ 
        Data Structure that mimics the implementation and performance of an
        implementation by an object oriented language such as Java or C++.
        Python dictionaries would honestly do this so much better.
    """

    # the constructor is always named __init__ !
    def __init__(self, initial_size=10):
        """ the constructor for objects of type Date """
        self.size_ = 0
        self.buckets_ = initial_size
        self.reallocations_ = 0
        self.collisions_ = 0
        self.maximal_ = 0
        self.table_ = [None]*initial_size
        self.MAX_LOAD = 1
        for i in range(initial_size):
            self.table_[i] = LinkedList()

    # the "printing" function is always named __repr__ !
    def __str__(self):
        """ This method returns a string representation for the
            object of type HashSet that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        return_str = '[ '
        for ll in self.table_:
            return_str += ll.__str__() + ', '

        return_str = return_str[:-2] + ']'
        return return_str

    def exists(self, value):
        """ 
        Checks if value exists in table.
        Input: Value to check
        Output: Boolean
        """
        hash_index = hash1(value)%self.buckets_
        listatindex = self.table_[hash_index]

        for item in Iterator(listatindex):
            if item == value:
                return True

        return False


    def resize(self):
        temp_holder = []
        tbl = list(filter(lambda x: x is not None, self.table_))
        
        self.table_ = [None]*len(self.table_)*2
        for i in range(len(self.table_)):
            self.table_[i] = LinkedList()
        self.buckets_ *= 2
        self.size_ = 0
        self.collisions_ = 0
        self.maximal_ = 0
        self.reallocations_ += 1
        
        for ll in tbl:
            for item in Iterator(ll):
                self.insert(item)

    # here is an example of a "method" of the Date class:
    def insert(self, value):
        """ Inserts value into table """
        if (self.exists(value)):
            print("Value already exists in Set!")
            return
        
        hash_index = hash1(value)%self.buckets_

        listatindex = self.table_[hash_index]
        if listatindex.size() != 0:
            self.collisions_ += 1

        listatindex.add(value)
        self.size_ += 1

        if listatindex.size() > self.maximal_:
            self.maximal_ = listatindex.size()

        if self.size_/self.buckets_ >= self.MAX_LOAD:
            self.resize()

    def collisions(self):
        return self.collisions_

    def reallocations(self):
        return self.reallocations_

    def maximal(self):
        return self.maximal_

    def size(self):
        return self.size_
    
    def buckets(self):
        return self.buckets_

def main():
    hs = HashSet()
    print(hs)
    hs.insert('abc')
    print(hs.maximal())
    print(hs)
    hs.insert('def')
    print(hs)
    hs.insert('cba')
    print(hs)
    hs.insert('fed')
    print(hs)
    hs.insert('ghi')
    print(hs)
    hs.insert('ihg')
    print(hs)
    hs.insert('jkl')
    print(hs)
    hs.insert('lkj')
    print(hs)
    print(hs.maximal())
    print(hs.size())
    print(hs.buckets())
    hs.insert('mno')
    print(hs)
    print(hs.reallocations())
    hs.insert('onm')
    print(hs)
    print(hs.maximal())
    print(hs.size())
    print(hs.buckets())
    print(hs.collisions())
    print(hs.reallocations())
    

if __name__ == "__main__":
    main()