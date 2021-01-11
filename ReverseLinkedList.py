from LinkedList import LinkedList
def reverseLinkedList(head):
    prev = None
    cur = head
    while cur and cur.next:
        next_node = cur.next 
        cur.next = prev 
        prev = cur 
        cur = next_node
    cur.next = prev
    return cur