# The following algorithm takes care of following edge cases.
# 1. if head is None
# 2. if head is val 
# 3. if last element is the val
# 4. if head is val
# 5. all elements has same val
# 6. mutiple nodes have same val

#approach 1 using dummy pointer
def removeDuplicates(head, val):
    dummy_head = ListNode(-1)
    dummy_head.next = head 
    runner = dummy_head
    while runner.next:
        if runner.next.val == val:
            runner.next = runner.next.next
        else:
            runner = runner.next 
    return dummy_head.next 


#approach 2 without using dummy pointer 
def removeDuplicates2(head, val):
    while head and head.val == val:
        head = head.next 
    runner = head
    while runner:
        if runner.next and runner.next.val == val:
            runner.next = runner.next.next
        else:
            runner = runner.next 
    return head 