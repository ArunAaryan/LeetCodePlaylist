# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        zigzag = False
        while q:
            current_level = []
            for _ in range(len(q)): # to run only for current length
                if zigzag:
                    node = q.pop()
                    current_level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                    
                else:
                    node = q.popleft()
                    current_level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(current_level)
            zigzag = not zigzag
        return res
                    


 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

s = Solution()
res = s.zigzagLevelOrder(root)

print(res)

                