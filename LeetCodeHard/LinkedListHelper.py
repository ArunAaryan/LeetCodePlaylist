class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def addNode(self, val):
        if not self.head:
            self.head = Node(val)
            return self.head
        else:
            cur = self.head 
            while cur.next:
                cur = cur.next 
            else:
                cur.next = Node(val)
            return cur.next
    def arrayToList(self, arr):
        for i in arr:
            self.addNode(i)
        return self.head

    @classmethod
    def arrayToListC(cls, arr):
        cur = head = Node(arr[0])
        for idx in range(1, len(arr)):
            cur.next = Node(arr[idx])
            cur = head.next
        return head




    def printList(self):
        cur = self.head 
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
    @classmethod
    def printElements(cls, head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print("")
        
