#day 5
# approach 1
def removeDuplicates(head):
    cur = head
    while cur:
        if cur.next and cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next 
    return head 


#same approach

def removeDuplicates1(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next 
    return head 