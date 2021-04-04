from LinkedListHelper import LinkedList, Node
class Solution:
    def removeNthFromEnd(self, head, k):
        dummy = Node(-1) #create this for case where k is same as the length of linkedlist
        dummy.next = head
        l = 0
        cur = head
        while cur:#iterate to find the length of list
            cur = cur.next 
            l += 1
        l -= k #find which element to delete
        first = dummy
        while l > 0:#iterate till the element -1, so as to change the next pointer of previous element 
            #works well even with the first element, since l = 0 , first element counts as 1
            l -= 1
            first = first.next
        first.next = first.next.next 
        head = dummy.next
        return dummy.next #return the actual head 
    def removenode1pass(self, head, n):
        dummy = Node(-1) 
        dummy.next = head
        fast= dummy
        slow = dummy
        while n:
            fast = fast.next
            n -= 1
        print(fast.val,'fast.val')
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        print(slow.val,'slow.val')
        slow.next = slow.next.next
        return dummy.next
l = LinkedList()
l.arrayToList([1,2,3,4,5,6,7,8,9,10])
l.printList()
print()

s = Solution()
# res = s.removeNthFromEnd(l.head,5)
res = s.removenode1pass(l.head, 10)
while res:
    print(res.val, end=" ")
    res = res.next

# l.printList()






        