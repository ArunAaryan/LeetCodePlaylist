from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, templist):
            if target < 0:
                return
            elif target == 0:
                res.append(templist[:])
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i -1]:
                        continue
                    templist.append(candidates[i])
                    backtrack(i + 1, target - candidates[i], templist)
                    templist.pop()
                    # i += 1

        res = []
        candidates.sort()
        backtrack(0, target, [])
        return res

s = Solution()        
res = s.combinationSum2([10,1,2,7,6,1,5], target = 8)
print(res)