# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedListHelper import LinkedList, Node
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = Node(-1)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next 
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return dummy.next

    def recursive(self, head):
        if not head or not head.next:
            return head
        next_node = head.next.next
        temp = head
        head = head.next
        head.next = temp
        head.next.next = self.recursive(next_node)
        return head


l = LinkedList()
head = l.arrayToList([1,2,3, 4])
s = Solution()
res = s.swapPairs(head)
res = s.recursive(head)
LinkedList().printElements(res)