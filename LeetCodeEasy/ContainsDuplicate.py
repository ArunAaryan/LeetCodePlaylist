#Day 1
class Solution:
    def containsDuplicate(self, nums):
        unique = set(nums)
        if len(unique) < len(nums):
            return True
        else:
            return False

    def containsDuplicateUsingSort(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    