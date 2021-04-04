from LinkedListHelper import LinkedList

class Solution():
    def addTwoNumbers(self, l1, l2):
        carry = 0
        l3 =  LinkedList()
        while l1 or l2: #ex 1-2-3 and 3-4-5-6 where one list is longer than the other
            if l1: # there is digit in this place
               l1val = l1.val
               l1 = l1.next
            else:
                l1val = 0 #there is no digit in place
            
            if l2:
                l2val = l2.val
                l2 = l2.next 
            else:
                l2val = 0
            current_sum = l1val + l2val + carry 
            carry = current_sum // 10
            remainder = current_sum % 10
            l3.addNode(remainder) 
        #after the digits are added there could be an additional carry that is being left off.
        if carry:
            l3.addNode(carry)
        
        return l3.head

l1 = LinkedList()
l1.arrayToList([2,4,3])

l2 = LinkedList()
l2.arrayToList([5,6,4])

s = Solution()
res =  s.addTwoNumbers(l1.head, l2.head)
while res:
    print(res.val, end=' ')
    res = res.next



