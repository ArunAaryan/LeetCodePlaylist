# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {root:None}
        qu = [root]
        
        while p not in parent or q not in parent:
            node = qu.pop(0)
            
            if node.left:
                parent[node.left] = node
                qu.append(node.left)
            
            if node.right:
                parent[node.right] = node
                qu.append(node.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
            
        while q not in ancestors:
            q = parent[q]
        return q

    def lowestCommonAncestorRecursive(self, root, p, q):
        if not root:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        else:
            return right
        
        
root = TreeNode(3) 
p = root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
q = root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
s = Solution()
res = s.lowestCommonAncestor(root, p, q)
print(res.val)
