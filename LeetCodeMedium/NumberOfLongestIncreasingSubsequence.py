from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [0] * n
        counts = [1] * n
        for fast in range(1, n):
            for slow in range(fast):
                if nums[slow] < nums[fast]:
                    if lengths[slow] >= lengths[fast]:
                        lengths[fast] = lengths[slow] + 1
                        counts[fast] = counts[slow]
                    elif lengths[slow] + 1 == lengths[fast]:
                        counts[fast] += counts[slow]

        longest = max(lengths)
        ans = 0
        for i in range(n):
            if lengths[i] == longest:
                ans += counts[i]
        return ans

        
    
s = Solution()
res = s.findNumberOfLIS([1,3,5,4,7])
print(res)

        