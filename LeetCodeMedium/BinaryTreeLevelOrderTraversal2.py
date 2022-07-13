# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        current = [root]
        res = deque()
        while current:
            next_level = []
            res.appendleft([])
            for node in current: # this runs for all children at the current level
                res[0].append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
        return(list(res))

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res, queue = [], deque([(root, 0)]) 
        while queue:
            node, level = queue.popleft() # keeping track of current level using level variable which is 0 by default during deque initialization
            if node:
                if level == len(res): # len(res) returns the current level, as we are adding level + 1 for all children at same level
                    #some children have same level but only the first child will cause this condition, because we increase the length by appending [] to res
                    res.append([])
                res[level].append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        return res[::-1]
                
        
        
        
s = Solution()
res = s.levelOrderBottom()
print(res)

        