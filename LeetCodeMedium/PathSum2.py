# https://leetcode.com/problems/path-sum-ii/discuss/36829/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        def dfs(root, remSum,temp):
            if root:
                if not root.left and not root.right and remSum == root.val:
                    temp.append(root.val)
                    res.append(temp)
                dfs(root.left, remSum - root.val, temp +[root.val]) 
                dfs(root.right, remSum - root.val, temp + [root.val]) 
        dfs(root, targetSum, [])
        return res
    def pathsum2(self, root, targetSum):
        if not root:
            return []
        res = []
        queue = deque([(root, root.val, [root.val])])
        while queue:
            root, value, currentList = queue.popleft()
            if not root.left and not root.right and value == targetSum:
               res.append(currentList)
            if root.left:
                currentList.append(root.left.val)
                queue.append((root.left, value + root.left.val, currentList ))
            if root.right:
                currentList.append(root.left.right)
                queue.append((root.right, value + root.right.val, currentList))
        return res
    # implemented by me
    def pathSumMyImplementation(self, root, targetSum):
        if not root:
            return []
        q = deque([(root, targetSum - root.val, [] )])

        res = []
        while q:
            currentNode, targetSum, currentPath = q.popleft()
            if not currentNode.left and not currentNode.right and targetSum == 0:
                currentPath.append(currentNode.val)
                res.append(currentPath)
                
            if currentNode.left:
                q.append((currentNode.left, targetSum - currentNode.left.val , currentPath + [currentNode.val]))
            if currentNode.right:
                # currentPath.append(currentNode.val)
                q.append((currentNode.right, targetSum - currentNode.right.val, currentPath + [currentNode.val]))
        return res
        

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

s = Solution()
res = s.pathsum2(root, 22)
print(res)