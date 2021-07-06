from heapq import nlargest 
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        return nlargest(k, c.keys(), key = c.get)




s = Solution()
res = s.topKFrequent([3,0,1,0],2)
print(res)


        