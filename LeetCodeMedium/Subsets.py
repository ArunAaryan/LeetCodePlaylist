from typing import List
class Solution:
    def __init__(self):
        self.st =  0
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

    #general solution for subsets
    def subsets2(self,nums):
        
        nums.sort()
        def backtrack(res, templist, nums, start):
            self.st += 1
            res.append(templist.copy())
            i = start 
            while ( i < len(nums)):
                templist.append(nums[i])
                backtrack(res, templist, nums, i+1)
                templist.pop()
                i += 1

        res = []
        backtrack(res, [], nums, 0) 
        return res 



s = Solution()
# s.subsets([1,2,2])
res = s.subsets2([3, 4,7,9])
print(s.st)
# print(res)
#similar problem solutions in python
#https://leetcode.com/problems/subsets/discuss/429534/General-Backtracking-questions-solutions-in-Python-for-reference-%3A