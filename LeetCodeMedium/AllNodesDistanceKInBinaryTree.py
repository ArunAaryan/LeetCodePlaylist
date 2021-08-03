# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root, target, k):
        if not root:
            return []
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        q = deque([(target, 0)])
        visited = {target}
        while q:
            if q[0][1] == k:
                res = []
                for node, dist in q:
                    res.append(node.val)
                return res
            node, distance = q.popleft()
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, distance + 1))
        return [] 