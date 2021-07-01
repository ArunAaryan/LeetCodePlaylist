from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(tempstring, start, end):
            if len(tempstring) == 2 * n:
                res.append(tempstring)
                return
            if start < n:
                backtrack(tempstring +"(", start + 1, end)
            
            if end < start:
                backtrack(tempstring + ")", start, end + 1)

        res =[ ]
        backtrack("", 0 , 0)
        return res
s = Solution()
res = s.generateParenthesis(2)
print(res)

        