from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, templist):
            if target < 0:
                return 
            elif target == 0:
                res.append(templist[:])
                # return
            else:
                i = start 
                while i < len(candidates):
                    templist.append(candidates[i])
                    backtrack(i, target - candidates[i], templist)
                    templist.pop()
                    i += 1

        res = []
        #nums.sort() optimization but not scaling
        backtrack(0, target, [])
        return res

s = Solution()
res =  s.combinationSum([2,3,6,7],7)
print(res)
        


        