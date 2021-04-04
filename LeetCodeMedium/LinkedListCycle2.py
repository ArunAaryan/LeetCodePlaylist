from LinkedListHelper import LinkedList
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        #Alternatively use can use the below line, because the condition must have exited because of it
        #If the statement slow == fast occurred due to the cycle the program flow would not reach the 
        #else clause
        #the program would reach the else clause only when the while failed after completing the loops or the statement lead to false
        # if not fast or fast.next:
        #     return None

        slow = head 
        while slow != fast:
            slow = slow.next 
            fast = fast.next
        return slow
        
l = LinkedList()
l.addNode(1)
l.addNode(2)
node = l.addNode(3)
l.addNode(4)
node2 = l.addNode(5)
node.next = node


s = Solution()
res = s.detectCycle(l.head)
if not res:
    print( "No Cycle")
else: 
    print("Cycle occurred at " + str(res.val))