# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedListHelper import LinkedList

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # partition till middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('Slow value',slow.val)

        #reverse from middle
        prev , cur = None, slow
        while cur:
            next_node = cur.next 
            cur.next = prev
            prev = cur
            cur = next_node
        
        # merge the reversed and original list in alternate order
        first = head
        second = prev
        while second and second.next:
            first_next = first.next
            first.next = second 
            first = second
            second = first_next

    def reorderConcise(self, head):
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        cur, prev = slow, None
        while cur:
            prev, cur.next, cur= cur, prev, cur.next
        
        first, second = head, prev
        while second and second.next:
            first.next, first = second, first.next 
            second.next, second = first, second.next 
        
l = LinkedList()
l.arrayToList([1,2,3,4,5,6,7,8,9,10])
s = Solution()
s.reorderConcise(l.head)
LinkedList().printElements(l.head)
