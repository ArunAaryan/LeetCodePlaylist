#Day 1
class Solution:
    def findDisappearedNumbers(self, nums):
        all_set = set(range(1, len(nums)+1))
        nums_set = set(nums)
        return all_set - nums_set
    
    

s = Solution()
res = s.findDisapearedNumbersUsingMarking([1,1,2])
print(res)

             
