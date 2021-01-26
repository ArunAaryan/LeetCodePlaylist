#Day 1
class Solution:
    def containsDuplicate(self, nums):
        unique = set(nums)
        if len(unique) < len(nums):
            return True
        else:
            return False
        