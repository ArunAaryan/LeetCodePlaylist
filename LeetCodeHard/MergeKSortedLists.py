# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2 
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dh = cur = ListNode(-1)
        while l and r:
            if l.val < r.val:
                cur.next = l 
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next 
        cur.next = l or r 
        return dh.next 
        
# other solutions
    # def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

# from Queue import PriorityQueue

# class Solution(object):
    # def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
 
from LinkedListHelper import LinkedList 
first = LinkedList.arrayToListC([1,2,4])
second = LinkedList.arrayToListC([3,4,5])
third = LinkedList.arrayToListC([2,3,6])
s = Solution()
res = s.mergeKLists([first, second, third])
while res:
    print(res.val)            
    res = res.next
