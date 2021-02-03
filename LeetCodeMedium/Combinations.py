from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(templist, start, k):
            if k == 0:
                res.append(templist[:])
                return  
            i = start
            while i <= n: #i <= n-k + 1 to optimize
                templist.append(i)
                backtrack(templist,i+1, k-1)
                templist.pop()
                i += 1
        res = []
        backtrack([], 1, k)
        return res
        

s = Solution()
res = s.combine(4,2)
print(res)