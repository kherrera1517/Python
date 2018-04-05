from Node import *

class BST:
    """Constructor for objects of type BST"""
    def __init__(self, root_value):
        self.root = Node(root_value)
        self.left = None
        self.right = None
        

    def __repr__(self):
        """Method returns a string representation for an object of type Node"""

        s = ""

        return s

    

    # def insert(self, value):
    #     n = Node(value)
    #     if self.root < n:
    #         if self.right is None:
    #             self.right = n
    #         else insert
