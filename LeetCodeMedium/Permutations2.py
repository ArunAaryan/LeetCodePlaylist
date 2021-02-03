from typing import List
class Solution:
    def __init__(self):
        self.count = 0
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(templist):
            self.count += 1
            if len(templist) == len(nums):
                res.append(templist[:])
            else:
                for i in range(len(nums)):
                    if used[i] or i > 0 and nums[i] == nums[i - 1] and not used[i -1]:
                        continue
                    used[i] = True
                    templist.append(nums[i])
                    backtrack(templist)
                    used[i] = False 
                    templist.pop()


        res =[]
        nums.sort()
        used = [False] * len(nums)
        backtrack([])
        return res

    



        res = []
        nums.sort()
        used = [False] * len(nums)
        backtrack([])
        return res

s = Solution()
res = s.permuteUnique([3,3,0,3])
print(s.count)
print(res)