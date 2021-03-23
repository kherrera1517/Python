#scratch work

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr1 = l1
        curr2 = l2
        currSum = curr1.val + curr2.val
        carry = currSum//10
        currSum = currSum%10
        returnNode = ListNode(currSum)
        prevNode = returnNode
        
        
        #change l1 and l2 lul
        while curr1.next != None and curr2.next != None:
            curr1 = curr1.next
            curr2 = curr2.next
            currSum = curr1.val + curr2.val + carry
            carry = currSum//10
            currSum = currSum%10
            currNode = ListNode(currSum)
            prevNode.next = currNode
            prevNode = currNode
            
        return returnNode

node1a = ListNode(2)
node1b = ListNode(4)
node1c = ListNode(3)
node1b.next = node1c
node1a.next = node1b

node2a = ListNode(5)
node2b = ListNode(6)
node2c = ListNode(4)
node2b.next = node2c
node2a.next = node2b
