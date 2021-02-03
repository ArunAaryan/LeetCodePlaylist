from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, templist):
            if len(templist) == len(nums):
                res.append(templist.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] in templist: continue
                    templist.append(nums[i])
                    backtrack(nums, res, templist)
                    templist.pop()
        res = []
        backtrack(nums, res, [])
        return res

s = Solution()
print(s.permute([1,2,3]))

        