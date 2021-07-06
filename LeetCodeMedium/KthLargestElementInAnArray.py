from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def findKthLargest(self, nums, k):
        heap =[]
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        print(heap)
        return(heappop(heap))
           



s = Solution()
res = s.findKthLargest([3,2,3,1,2,4,5,5,6,7],4)
print(res)
        