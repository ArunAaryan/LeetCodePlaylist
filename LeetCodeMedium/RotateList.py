# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedListHelper import LinkedList, Node
class Solution:
    def rotateRight(self, head, k):
        if not head or k == 1 or k == 0:
            return head
        
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        cur = head
        print(l)
        k = k% l
        print(k)
        for _ in range(l - k -1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        cur = new_head
        while cur.next:
            cur = cur.next
        cur.next = head
        head = new_head
        return head
    
    def rotateRight(self, head, k): #this is fast and slow pointer approach
        

             



l = LinkedList()
head =  l.arrayToList([1,2,3,4,5])
s = Solution()
res = s.rotateRight(head, 5)
LinkedList().printElements(res)

# print(4 %3)

        