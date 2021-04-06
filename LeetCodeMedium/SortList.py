from LinkedListHelper import LinkedList, Node
class Solution:
    def getMid(self, head):
        midPrevious = None
        while head and head.next: #to check atleast if there are two elements, only then 
            #we can return one mid and midPrevious
            if not midPrevious:
                midPrevious = head
            else:
                midPrevious = midPrevious.next
            head = head.next.next
        mid = midPrevious.next
        midPrevious.next = None
        return mid

    def merge(self, l1, l2):
        dummyHead = Node(-1) 
        tail = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummyHead.next
        
                
                

    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.getMid(head) # Unlinks the element from previous element and returns the mid element so that
        #we can continue dividing from the mid element 
        left= self.sortList(head) # divide the left part
        right = self.sortList(mid) # divide the right part
        return self.merge(left, right)


l = LinkedList()
l.arrayToList([1,2,3,4,5])

s = Solution()
res = s.sortList(l.head)
LinkedList().printElements(res)

