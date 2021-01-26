

class TreeNode():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class solution():
    def MergeTwoBinaryTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.MergeTwoBinaryTrees(root1.left, root2.left)
        root2.right = self.MergeTwoBinaryTrees(root1.right, root2.right)
        return root1

    def MergeTwoBinaryTreesIterative(self, root1, root2):
        if not root1:
            return root2
        stack = []
        stack.append((root1, root2))
        while stack:
            t1, t2 = stack.pop(0)
            if not t2:
                continue
            t1.val += t2.val
            if not t1.left:
                t1.left = t2.left
            else:
                stack.append((t1.left, t2.left))
            if not t1.right:
                t1.right = t2.right
            else:
                stack.append((t1.right, t2.right))
        return t1
            
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(4)
root2 = TreeNode(2)
root2.left = TreeNode(5)
root2.left.left = TreeNode(7)

s = solution()
# s.MergeTwoBinaryTrees(root1, root2)
s.MergeTwoBinaryTreesIterative(root1, root2)

def printTree(root):
    if not root:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

printTree(root1)

