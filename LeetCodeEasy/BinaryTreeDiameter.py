class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.diameter = 0

    def dfs(self,root):
        val = self.dfs_helper(root)
        return(self.diameter,val)

    def dfs_helper(self,root):
        if not root:
            return 0
        l_height = self.dfs_helper(root.left)
        r_height = self.dfs_helper(root.right)
        self.diameter = max(self.diameter, l_height + r_height)
        return max(l_height , r_height )+1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right= TreeNode(7)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

root.right = TreeNode(3)
root.right.right = TreeNode(6)
s = Solution()
print(s.dfs(root))