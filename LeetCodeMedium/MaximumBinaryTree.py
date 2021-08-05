# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def findMax(nums, l, r):
            m = l 
            for i in range(l, r):
                if nums[i] > nums[m]:
                    m = i 
            return m
        def construct(nums, l, r):
            if l == r:
                return None
            m = findMax(nums, l, r)
            root = TreeNode(nums[m])
            root.left = construct(nums, l, m)
            root.right = construct(nums, m + 1, r)
            return root
        return (construct(nums, 0, len(nums)))
         
    def constructMaximumBinaryTree(nums):
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
            stack.append(node)
        
        return stack[0]
        
            
        