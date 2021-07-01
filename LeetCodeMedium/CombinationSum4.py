from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.count = 0
        res = 0
        # res = self.dfs(nums, target, res)
        dp = [-1] * (target + 1)
        dp[0] = 1
        res = self.dfsWithMemo(nums, target, res, dp)
        return (res, self.count)
    
    def dfsnaive(self, nums, target, res):
        self.count += 1
        if target == 0:
            return 1
        
        for num in nums:
            if target >= num:
                res += self.dfsnaive(nums, target - num, 0)    
    
        return res

    def dfsWithMemo(self, nums, target, res, dp):
        self.count += 1
        if dp[target] != -1:
            return dp[target]
        for num in nums:
            if target >= num:
                res += self.dfsWithMemo(nums, target - num, 0, dp)
        
        dp[target] = res 
        return res

def dfsIterative(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for current in range(1, target+1):
        for num in nums:
            if current - num >= 0:
                dp[current] += dp[current - num] 
    return dp[target]


s = Solution()
res, count = s.combinationSum4([1,2,3,4],3)

print(dfsIterative([1,2,3], 4))

