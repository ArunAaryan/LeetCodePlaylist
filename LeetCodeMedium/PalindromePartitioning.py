from typing import List
class Solution:
    def partitionBacktrack(self, s: str) -> List[List[str]]:
        def isPalindrome(start, end, s):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
    
        def backtrack(start, tempList, s):
            if start == len(s):
                res.append(tempList[:])
                return 
            else:
                for i in range(start, len(s)):
                    if isPalindrome(start, i, s):
                        tempList.append(s[start:i+1])
                        backtrack(i + 1, tempList, s)
                        tempList.pop()

        res = [] 
        backtrack(0, [], s)
        return res

s = Solution()
res = s.partitionBacktrack("abc")
print(res)
