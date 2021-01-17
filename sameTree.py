#day 8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
#recursive solution
def sameTreeRecursive(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    else:
        return p.val == q.val and  sameTreeRecursive(p.left, q.left) and sameTreeRecursive(p.right, q.right)
#iterative solution easy to understand

def sameTreeIterative(p, q):
    stack = [(p,q)]
    while stack:
        first, second = stack.pop()
        if not first and not second:
            pass
        elif not first or not second:
            return False
        else:
            stack.append((first.left, second.left))
            stack.append((first.right, second.right))
    return True
root1 = TreeNode(1)
# root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(sameTreeRecursive(root1, root2))

