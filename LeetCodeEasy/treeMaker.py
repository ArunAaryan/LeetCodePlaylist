class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
    
class Builder():

    def levelOrderBuilder(self,arr, root, root_pos, arr_len):
        if root_pos < arr_len:
            root = TreeNode(arr[root_pos])
            root.left = self.levelOrderBuilder(arr, root.left, 2 * root_pos + 1, arr_len)
            root.right = self.levelOrderBuilder(arr, root.right, 2 * root_pos + 2, arr_len)
            return root

    def  ReturnTreeRoot(self,arr):
        root = None
        root = self.levelOrderBuilder(arr,root, 0, len(arr)) 
        return root

    def printTree(self,root):
        if not root:
            return
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)

    def bfs(self, root):
        q = []
        q.append(root)
        while len(q):
            root = q.pop(0)
            print(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            

# b = Builder()
# root = b.ReturnTreeRoot([1,2,3,4,5,6,7,8,9,10])
# b.bfs(root)