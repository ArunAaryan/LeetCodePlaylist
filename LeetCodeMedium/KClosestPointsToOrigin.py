import math
from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points:
            ans = math.sqrt(point[0] * point[0] + point[1] * point[1])
            heappush(heap, (ans, point))
        
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
            
            
            
        
        