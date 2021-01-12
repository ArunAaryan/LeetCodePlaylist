#day 6
#approach 1 and approach 2 differ in logic for remaining elements in their lists
headn = n.addNode(-1)
def mergeSortedLinkedList(head1, head2, headn):
    p1 = head1
    p2 = head2
    new_list = headn
    while p1 and p2:
        if p1.data <= p2.data:
            new_list.next = p1 
            new_list = new_list.next 
            p1 = p1.next 
        else:
            new_list.next = p2 
            new_list = new_list.next 
            p2 = p2.next 
    while p1:
        new_list.next = p1
        new_list = new_list.next 
        p1 = p1.next 
    while p2:
        new_list.next = p2
        new_list = new_list.next 
        p2 = p2.next 


# mergeSortedLinkedList(head1, head2, headn)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = sort_list = ListNode(0)
        
        while(l1 and l2):
            if (l1.val < l2.val):
                sort_list.next = l1
                l1 = l1.next
                sort_list = sort_list.next
                
            elif (l1.val >= l2.val):
                sort_list.next = l2
                l2 = l2.next
                sort_list = sort_list.next
        # No need of loops since remainig lists are already intact.
        sort_list.next = l1 or l2
        return head.next