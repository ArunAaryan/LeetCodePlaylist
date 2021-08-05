# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        currentDepth = left = res = 0
        q = deque()
        q.append((root, 0, 0))
        while q:
            node, pos, depth = q.popleft()
            if node.left:
                q.append((node.left, pos * 2, depth + 1))
            if node.right:
                q.append((node.right, pos * 2 + 1, depth + 1))
            if currentDepth != depth:
                left = pos
                currentDepth = depth
            res = max(res, pos - left + 1)
        return res 
            
        
        