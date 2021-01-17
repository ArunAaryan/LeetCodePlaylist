def pathSum(root, sum):
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    sum -= root.val

    return pathSum(root.left, sum) or pathSum(root.right, sum)