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
    
    def rotateRightSF(self, head, k): #this is fast and slow pointer approach
        if not head or not head.next:
            return head
        def getLength(head):
            length = 1
            while head.next:
                head = head.next
                length += 1
            return length
        length = getLength(head)
        # print('length',length)
        rotateTimes = k % length

        if k == 0 or rotateTimes == 0:
            return head
        slow = head
        fast = head
        for _ in range(rotateTimes):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # cur = slow.next
        # slow.next = None
        # fast.next = head
        # head = cur
        head, fast.next, slow.next = slow.next, head, None
        return head
    
    def rotateUsingCircular(self, head, k):
        if not head or not head.next:
            return head
        
        cur = head
        l = 1 
        while cur.next:
            cur = cur.next
            l += 1
        cur.next = head
        temp = head
        for _ in range(l - k -1):
            temp = temp.next
        
        head = temp.next
        temp.next = None
        return head

l = LinkedList()
head =  l.arrayToList([1,2,3,4,5])

s = Solution()
# res = s.rotateRight(head, 5)
# res = s.rotateRightSF(head,2)
res = s.rotateUsingCircular(head, 2)
LinkedList().printElements(res)

# print(4 %3)

        