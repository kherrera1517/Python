class Node:
    def __init__(self, value=None, nxt=None):
        self.val = value
        self.next = nxt
    
    def __str__(self):
        print_str = "( " + str(self.val) + " )"
        if self.next is None:
            return print_str
        else:
            return print_str + " -> "

    def has_next(self):
        if self.next is None:
            return False

        return True

class Iterator:
    def __init__(self, linked_list):
        self.prev = None
        self.curr = linked_list.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration()
        else:
            self.prev = self.curr
            self.curr = self.curr.next
            return self.prev.val

class LinkedList:
    """A Singly Linked List Class"""
    def __init__(self, ls=[]):
        if ls == []:
            self.head = None
        else:
            self.head = Node(ls[0])
            current_node = self.head
            for i in range(1,len(ls)):
                current_node.next = Node(ls[i])
                current_node = current_node.next

        self.size_ = len(ls)

    def __str__(self):
        current_node = self.head
        return_str = ""
        while(current_node is not None):
            return_str += current_node.__str__()
            current_node = current_node.next
        return return_str

    def size(self):
        return self.size_

    def add_first(self, value):
        newhead = Node(value, self.head)
        self.head = newhead
        self.size_ += 1

    #CAN ADD DEFAULT PARAMETER SO THAT ADD CAN ADD ANYWHERE ON THE LIST
    #if we add the change above, we can change add_first to be a wrapper func
    def add(self, value):
        """Adds to end of linked list"""
        if self.head is None:
            self.add_first(value)
        else:
            curr_node = self.head
            while(curr_node.has_next()):
                curr_node = curr_node.next
            curr_node.next = Node(value)
        
            self.size_ += 1
        
    def contains(self, value):
        if self.head is None:
            return False
        else:
            curr_node = self.head
            while(curr_node is not None):
                if curr_node.val == value:
                    return True
                curr_node = curr_node.next
            return False
    
    def delete(self, value):
        if self.head is not None and self.head.val == value:
            self.head = None
        else:
            prev_node = self.head
            current_node = self.head.next
            while(current_node is not None):
                if current_node.val == value:
                    prev_node.next = current_node.next
                    break
                else:
                    prev_node = current_node
                    current_node = current_node.next
        self.length -= 1




def main():
    ll = LinkedList([1,2,3,4,5])
    print(ll)
    print(ll.head)
    ll.add_first(0)
    print(ll)
    ll.add(6)
    print(ll)
    lils = LinkedList([])
    print(lils)
    lils.add(10)
    print(lils)
    print(ll.contains(42))
    print(lils.contains(10))
    ll.delete(3)
    print(ll)
    lils.delete(10)
    print(lils)
    ll.delete(6)
    print('ll is {}'.format(ll))
    print('the size of ll is {}'.format(ll.size()))
    # i = Iterator(ll)
    # print(next(i))

    for item in Iterator(ll):
        print(item)
    # i = iter(ll)
    # print(i.next())

if __name__ == "__main__":
    main()