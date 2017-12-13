"""Node Class"""
class Node:
    """Constructor for objects of type Node"""

    def __init__(self, data, left_child=None, right_child=None, hidden_data=None):
        self.data = data
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child
        self.hidden_data = hidden_data

    def __repr__(self):
        """Method returns a string representation for an object of type Node"""

        string = "( {} )".format(self.data)

        return string

    def __gt__(self, a):
        """Docstring"""
        return self.data > a.data

    def __lt__(self, a):
        """Docstring"""
        return self.data < a.data

    def add_child(self, node):
        """Docstring"""
        if self < node:
            if self.right_child is None:
                self.right_child = node
            else:
                print("Cannot add node. Node already has existing right child!")
        elif self > node:
            if self.left_child is None:
                self.left_child = node
            else:
                print("Cannot add node. Node already has existing left child!")
        else:
            print("Node with data already exists!")

    def get_data(self):
        """Docstring"""
        return self.data

if __name__ == "__main__":
    n2 = Node(6)
    n3 = Node(4)
    n1 = Node(5, n3, n2)
    print(n2)

    print(n2 > n1)
    print(n3 > n1)
    print(n3 < n1)

    n1.add_child(Node(7))
    n2.add_child(Node(4))