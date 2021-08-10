# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        self.treeIndex = 0
        hashmap = {}
        def createMap(inorder):
            for idx, val in enumerate(inorder):
                hashmap[val] = idx 

        def arrTree(left, right):
            if left > right:
                return None
            rootVal = preorder[self.treeIndex]
            root = TreeNode(rootVal)
            self.treeIndex += 1
            root.left = arrTree(left, hashmap[rootVal] -1)
            root.right = arrTree(hashmap[rootVal] + 1, right)
            return root
        createMap(inorder)
        print(hashmap)
        res = arrTree(0, len(preorder) -1 )
        return res




s = Solution()
res = s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
def inorder(root):
    if not root: return
    print(root.val)
    inorder(root.left)
    inorder(root.right)

        
        