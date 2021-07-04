class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, k):
        self.k = k
        self.res = None
        self.found = False
        self.helper1(root)
        return ("kth smallest "+ str(self.res))

    def helper(self, root):
        if self.found:
            return
        print(self.k)
        if not root:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.found = True
            self.res = root.val
            return
        self.helper(root.right)

    def helper1(self, root):
        print(self.k)
        if not root:
            return False
        if (self.helper1(root.left)):
            return True
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return True
        if self.helper1(root.right):
            return True
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right= Node(14)
root.right.right.left= Node(13)


s = Solution()
res = s.inorder(root,1)
print(res)
        
        
        