#Day 1
class Solution:
    def missingNumber(self, nums) -> int:
        val = len(nums)
        for i in range(len(nums)):
            val ^= nums[i]
            val ^= i
        return val
       
        
        