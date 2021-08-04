# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        cache = {0:1}
        self.result = 0

        self.dfs(root, targetSum, 0, cache)

        return self.result

    def dfs(self, root, target, curPathSum, cache):
        if not root:
            return 
        
        curPathSum += root.val
        oldPathSum = curPathSum - target
        self.res += cache.get(oldPathSum, 0)
        cache[curPathSum] = cache.get(curPathSum, 0) + 1

        self.dfs(root.left, target, curPathSum, cache)
        self.dfs(root.right, target, curPathSum, cache)

        cache[curPathSum] -= 1


        

        