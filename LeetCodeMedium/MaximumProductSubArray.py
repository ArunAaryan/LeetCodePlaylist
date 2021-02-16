from typing import List
import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      gmax = imax = imin = nums[0]
      
      for i in range(1, len(nums)):

        vals = (nums[i], nums[i] * imax, nums[i] * imin)
        imax = max(vals)
        imin = min(vals)
        
        gmax = max(gmax, imax)
        return gmax
    
    def maxProduct1(self, nums: List[int]) -> int:
        prod = 1
        gmax = -100000000
        for num in nums:
            prod *= num
            gmax = max(gmax, prod)
            if num == 0 : prod = 1
        prod = 1 
        for i in range(len(nums), 0, -1):
            prod *= num
            gmax = max(gmax, prod)
            if nums[i] == 0 : prod = 1
        return gmax



s = Solution()
res = s.maxProduct([0,2])
print(res)
# https://leetcode.com/problems/maximum-product-subarray/discuss/421525/Accepted-Python-Answer-using-in-place-multiplication




        