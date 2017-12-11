class Node:
    """Constructor for objects of type Node"""
    def __init__(self, value, left_child = None, right_child = None, hidden_value = None):
        self.value = value
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child
        self.hidden_value = hidden_value

    def __repr__(self):
        """Method returns a string representation for an object of type Node"""

        s = "( {} )".format(self.value)

        return s

    def __gt__(a, b):
        return a.value > b.value

    def __lt__(a, b):
        return a.value < b.value

    def add_child(self, Node):
        if self < Node:
            if self.right_child is None:
                self.right_child = Node
            else:
                print("Cannot add node. Node already has existing right child!")
        elif self > Node:
            if self.left_child is None:
                self.left_child = Node
            else:
                print("Cannot add node. Node already has existing left child!")
        else:
            print("Node with value already exists!")

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