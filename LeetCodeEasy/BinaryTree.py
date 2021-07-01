class BTNode():
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

    def printTree(self, node):
        q = []
        q.append(node)
        while q:
            r = q.pop(0)
            print(r.val)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        
    def preOrder(self, root):
        s = []
        cur = root
        while cur or s:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop(0)
            print(cur.val, end=' ')
            cur = cur.right
    
root = BTNode(1)
root.left = BTNode(2)
root.right = BTNode(3)
root.left.left = BTNode(4)
root.left.right = BTNode(5)
root.preOrder(root)

                
            