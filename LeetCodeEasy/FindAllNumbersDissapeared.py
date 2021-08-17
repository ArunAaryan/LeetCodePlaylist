#Day 1
class Solution:
    def findDisappearedNumbers(self, nums):
        all_set = set(range(1, len(nums)+1))
        nums_set = set(nums)
        return all_set - nums_set
        
    def findDisppearedNumbers(self, nums): 
        for i in range(len(nums)):
            num_index = abs(nums[i] - 1)
            if nums[num_index] > 0:
                nums[num_index] -= 1
        res = [] 
        for index, num in enumerate(nums):
            if num > 0:
                res.append(index + 1)
        return res
s = Solution()
# res = s.findDisapearedNumbersUsingMarking([1,1,2])
res = s.findDisppearedNumbers([1,1,2])
print(res)

             
