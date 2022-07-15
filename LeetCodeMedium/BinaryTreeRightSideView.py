# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56248/Python-easy-to-understand-BFS-solution-(level-by-level)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            last_val = 0
            for _ in range(len(q)):
                node = q.popleft()
                last_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(last_val)
        return res
    def rightSideViewDfs(self, root):
        self.ans = []
        
        def dfs(root, depth):
            if root == None: return
            if depth == len(self.ans):  # When we meet this `depth` for the first time, let's add the first node as the right side most node.
                self.ans.append(root.val)
            dfs(root.right, depth + 1)  # Go right side first
            dfs(root.left, depth + 1)
            
        dfs(root, 0)
        return self.ans

            
        