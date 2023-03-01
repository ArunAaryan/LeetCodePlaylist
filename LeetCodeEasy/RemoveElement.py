class Solution:
    def removeElement(self, nums, val):
        start = 0
        for end in range(len(nums)):
            if nums[end] != val:
                nums[start] = nums[end]
                start += 1
        return start
s = Solution()
nums= [1,2,1,3,1, 4]
ans = s.removeElement(nums, 1)
print(nums[:ans])
