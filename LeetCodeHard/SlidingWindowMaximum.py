# https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []
        for pos, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(pos)
            if q[0] == pos - k:
                q.popleft()
            if pos >=  k - 1:
                res.append(nums[q[0]])
        return res

s = Solution()
res = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3)
print(res)
            
       