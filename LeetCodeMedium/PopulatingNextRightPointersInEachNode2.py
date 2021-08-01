# Definition for a Node.
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/961868/Python-O(n)-solution-explained
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root):
        if not root:
            return root
        q = deque([root]) 
        while q:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
                current_level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for i in range(len(current_level) - 1):
                current_level[i].next = current_level[i + 1]
        return root
    def connectspace(self, root):
        node = root
        while node:
            next_tail = dummy = Node(0)
            while node:
                if node.left:
                    next_tail.next = node.left
                    next_tail = next_tail.next
                if node.right:
                    next_tail.next = node.right
                    next_tail = next_tail.next
                node = node.next
            node = dummy.next
               
        return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
s = Solution()
res = s.connectspace(root)