from collections import Counter
from heapq import heappush, heappop 
class Solution:
    def reorganizeString(self, s):
        c = Counter(s)
        max_freq = c.most_common(1)[0][1]
        if 2 * max_freq -1 > len(s):
            return ""
        else:
            heap = []
            res = ""
            for char, freq in c.items():
                heappush(heap, (freq * -1, char))
            while heap:
                freq, char = heappop(heap)
                if not res or char != res[-1]:
                    res += char
                    if freq != -1:
                        heappush(heap, (freq + 1, char))
                else:
                    new_freq, new_char = heappop(heap)
                    res += new_char
                    heappush(heap, (freq, char))
                    if new_freq != -1:
                        heappush(heap, (new_freq + 1, new_char))
        return res

s = Solution()
res = s.reorganizeString('aabca')
print(res)