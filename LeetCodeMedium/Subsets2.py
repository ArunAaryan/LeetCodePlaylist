# Backtracking can be solved always as follows:
# Pick a starting point.
# while(Problem is not solved)
#     For each path from the starting point.
#         check if selected path is safe, if yes select it
#         and make recursive call to rest of the problem
#         before which undo the current move.
#     End For
# If none of the move works out, return false, NO SOLUTON.
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, templist, start):
            res.append(templist.copy())
            i = start
            while i < len(nums):
                # handle the first element for 'list index out of range' 0 -1
                if nums[i] == nums[i - 1] and i > start:
                    i += 1
                    continue
                templist.append(nums[i])
                backtrack(nums, res, templist, i + 1)
                templist.pop()
                i += 1
        res = []
        nums.sort()
        backtrack(nums, res, [], 0)
        return res


s = Solution()
res = s.subsetsWithDup([1, 2, 2])
print(res)
