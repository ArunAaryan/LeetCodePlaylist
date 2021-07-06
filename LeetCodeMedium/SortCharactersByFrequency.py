from heapq import  heappush, heappop
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for key in c:
            heappush(heap, (-1 * c[key], key))
        string = ''
        while heap:
            count, char = heappop(heap)
            string += char * (-1 * (count))
        return string

s = Solution()
res = s.frequencySort('dabcdabdad')
print(res)



        