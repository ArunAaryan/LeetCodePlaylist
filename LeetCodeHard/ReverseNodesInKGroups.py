# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11440/Non-recursive-Java-solution-and-idea
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, begin, end):
        prev = None
        cur = begin.next
        first_node = cur
        while cur != end:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        begin.next = prev
        first_node.next = cur
        return first_node
            

    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1:
            return head
        dh = ListNode(-1) 
        dh.next = head
        begin = dh
        i = 0
        while head:
            i += 1
            if i % k == 0:
                end = head.next
                begin = self.reverse(begin, end)
                head = begin.next
            else:
                head = head.next
        return dh.next

from LinkedListHelper import LinkedList
l = LinkedList()
head = l.arrayToList([1,2,3,4,5])
s = Solution()
res = s.reverseKGroup(head, 3)
while res:
    print(res.val)
    res = res.next
