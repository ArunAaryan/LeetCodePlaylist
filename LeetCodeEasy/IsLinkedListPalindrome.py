from LinkedList import LinkedList

l = LinkedList()
h = l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(2)
l.addNode(1)

def isPalindrome(head):
    slow = fast = head
    rev = None
    while fast and fast.next:
        fast = fast.next.next
        tmp = rev
        rev = slow
        slow = slow.next
        rev.next = tmp
    if fast:
        slow = slow.next 
    while rev and rev.data == slow.data:
        rev = rev.next 
        slow = slow.next 
    return not rev
print(isPalindrome(h))