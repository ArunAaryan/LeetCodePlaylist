# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        if not root: return True
        def dfs(root, left, right):
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False
            return (dfs(root.left, left, root.val) and dfs(root.right, root.val, right)) 
        return dfs(root, float('-inf'), float('inf'))
        
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
                
s = Solution()
res = s.isValidBST(root)
print(res)
                
        
        