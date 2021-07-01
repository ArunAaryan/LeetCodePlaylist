from typing import List
class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     return max(self.rob1(nums), self.rob2(nums))
    
    # def rob1(self, nums):
    #     prev = prevprev = 0
    #     for i in range(len(nums) -1):
    #         temp = prev
    #         prev = max(prev, prevprev + nums[i])
    #         prevprev = temp
    #     return prev
    
    # def rob2(self, nums):
    #     prev = prevprev = 0
    #     for i in range(1, len(nums)):
    #         temp = prev
    #         prev = max(prev, prevprev + nums[i])
    #         prevprev = temp
    #     return prev

    def robcheck(self, nums: List[int]) -> int:
        n = len(nums)
        first = self.rob1(nums, 0,n - 1)
        second = self.rob1(nums,1,n )
        return max(first, second)
        
    def rob1(self,nums, start, end):
        prev = cur = 0
        for i in range(start, end):
            temp = cur
            cur = max(cur, prev + nums[i])
            prev = temp
        return cur
    
      
        
s = Solution()
res = s.rob([2,3,2])
print(res)
        
         

        
        