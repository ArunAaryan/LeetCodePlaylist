from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target, templist, k):
            if target < 0:
                return 
            elif target == 0 and k == 0:
                res.append(templist[:])
                return 
            else:
                for i in range(start, 10):
                    templist.append(i)
                    backtrack(i + 1, target - i, templist, k - 1)
                    templist.pop()

        res =[]
        backtrack(1, n, [], k)
        return res
    #some refactor
    def combinationSum3N(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, target, templist, k):
            if len(templist) == k and target == 0:
                res.append(templist[:]) 
                return 
            for i in range(start, 10):
                templist.append(i)
                backtrack(i + 1, target - i,templist, k)
                templist.pop()
        res = []
        backtrack(1, n, [], k)
        return res


s = Solution()
res = s.combinationSum3N(9, 45)
print(res)
        
