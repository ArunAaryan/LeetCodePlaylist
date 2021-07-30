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
            for node in current:
                res[0].append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
        return(list(res))


s = Solution()
res = s.levelOrderBottom()
print(res)

        