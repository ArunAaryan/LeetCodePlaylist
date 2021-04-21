from LinkedListHelper import LinkedList, Node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        dh = Node(-1)
        dt = Node(-2)
        dhc = dh
        dtc = dt
        idx = 1
        while head:
            if idx % 2 == 1:
                dh.next = head
                dh = dh.next
            else:
                dt.next = head
                dt = dt.next
            idx += 1
            head = head.next
        dh.next = dtc.next
        dt.next = None
        return dhc.next

    def oddEvenListWithoutIdx(self, head):
        if not head:
            return head
        odd = head
        even = head.next
        evenhead = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head
        
       
       
l = LinkedList()
head = l.arrayToList([1,2,3,4,5]) 
s = Solution()
res = s.oddEvenListWithoutIdx(head)
LinkedList().printElements(res)