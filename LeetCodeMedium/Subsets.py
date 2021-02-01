from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.findSubset(nums, 0, res, subset)
        print(res)
    def findSubset(self, nums, idx, res, subset):
        if idx >= len(nums):
            res.append(subset.copy())
            return 
        subset.append(nums[idx])
        self.findSubset(nums, idx+1, res, subset)
        subset.pop()
        self.findSubset(nums, idx+1, res, subset)
        return  

s = Solution()
s.subsets([1,2,3])
#similar problem solutions in python
#https://leetcode.com/problems/subsets/discuss/429534/General-Backtracking-questions-solutions-in-Python-for-reference-%3A