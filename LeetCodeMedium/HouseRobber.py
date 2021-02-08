#https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
from typing import List
class Solution:
    def robNaive(self, nums: List[int]) -> int:
        return self.recur(nums, len(nums) - 1)
    

    def recur(self, nums, index):
        if index < 0:
            return 0
        else:
            return max(self.recur(nums, index -2) + nums[index], self.recur(nums, index-1))

    def rob(self, nums: List[int]) -> int:
        self.memo = [False] * (len(nums) + 1)
        return self.dp(nums, len(nums) -1, self.memo)

    def dp(self, nums, index, memo):
        if index < 0:
            return 0
        elif memo[index]:
            return memo[index]
        else:
            res = max(self.dp(nums, index -2, memo) + nums[index], self.dp(nums, index - 1, memo))
            memo[index] = res 
            return memo[index]
    
    def robIterativeDP(self, nums: List[int]) -> int:
        if not nums: return 0
        # self.memo = [0] * (len(nums) + 1)
        # self.memo[0] = 0
        # self.memo[1] = nums[1]
        # for idx, val in enumerate(nums):
        #     self.memo[idx + 1] = max(self.memo[idx], self.memo[idx - 1] + val)

        self.memo = [0] * len(nums)
        self.memo[0] = nums[0]
        self.memo[1] = nums[1]
        for i in range(2, len(nums)):
            self.memo[i] = max(self.memo[i - 1], self.memo[i - 2] + nums[i])
        return self.memo[len(nums) - 1]

        
        return self.memo[len(nums)]

    def robStateVariables(self, nums: List[int]) -> int:
        prev = 0
        prevprev = 0
        for num in nums:
            temp = prev 
            prev = max(prev, prevprev + num)
            prevprev = temp
        return prev
        
             
s = Solution()
res = s.robStateVariables([10,2,2 ,10,25,35])
print(res)

        


        