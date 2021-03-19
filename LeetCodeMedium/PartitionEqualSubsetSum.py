from typing import List
class Solution:
  def canPartition2D(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        #bitwise trick to check if a number is even or odd. Returns 1 if odd
        if total & 1:
            return False
        total  = total // 2 
        dp = [[False]*(total + 1) for _ in range(n+1)]
        #with element not included and for sum is 0 is possible by simply not using any element from nums
        #for all values of nums, getting sum is 0 is possible by simply not selecting that element
        for i in range(n + 1):
            dp[i][0] = True
        
        for val in range(1, n + 1):
            for cursum in range(1, total + 1):
                # dp[i - 1][j] means simply ignore the current element and take the best of previous element
                #dp[i - 1][j - nums[i - 1]] means with including the current element is it possible to 
                #get required sum and also check if removing current nums[i] was also true is previous state [j- nums[i - 1]]

                if cursum >= nums[val - 1]:
                    dp[val][cursum] = dp[val-1][cursum] or dp[val-1][cursum- nums[val - 1]]
                    # print(dp[val][cursum])
        return dp[n][total]

s = Solution()
res = s.canPartition2D([2,2,1,1])
print(res)


