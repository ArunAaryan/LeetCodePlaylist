# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedListHelper import LinkedList, Node
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or not head.next:
            return head
        dummy_head = Node(-1)
        dummy_head.next = head 
        cur = dummy_head
        pos = 0
        while pos + 1 < left:
            cur = cur.next
            pos = pos + 1
        left_prev = cur
        left_node = cur.next
        cur = cur.next
        pos = pos + 1
        prev = None
        while pos <= right:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            pos += 1
        left_prev.next = prev
        left_node.next = next_node 
        return dummy_head.next

    def reverseBetween2(self, head, left, right):
        if not head or left == right:
            return head
        dummy_head = Node(-1)
        dummy_head.next = head
        cur = dummy_head
        for _ in range(left-1):
            cur = cur.next
        left_prev = cur
        
        cur = cur.next
        prev = None
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        left_prev.next.next = cur
        left_prev.next = prev
        return dummy_head.next

    def reverseBetween3(self, head, left, right):
        if not head or left == right:
            return head
        dummy = Node(-1)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next

        for _ in range(right - left ):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next


    def reverseBetween4(self, head, m, n):
        dummy, dummy.next = Node(0), head
        
        cur, prev = head, dummy
        for _ in range(m - 1):
            cur, prev = cur.next, prev.next
        
        for _ in range(n - m):
            cur.next.next, prev.next, cur.next = prev.next, cur.next, cur.next.next

        return dummy.next
        
l = LinkedList()
head = l.arrayToList([1,2,3,4,5])
s = Solution()
res = s.reverseBetween3(head, 1,4)
LinkedList.printElements(res)