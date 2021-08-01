# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque   
class Solution:
    def connect(self, root): # O(n) space where n is the  size of children at the deepest level
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
        if not root:
            return root
        current = root
        next_level_node = root.left
        while current.left:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
                current = current.next
            else:
                current = next_level_node
                next_level_node = current.left
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
s = Solution()
res = s.connect(root)

def check(root):
    if root:
        print(root.val)
        if root.next:
            check(root.next)
check(root.left.left)

        