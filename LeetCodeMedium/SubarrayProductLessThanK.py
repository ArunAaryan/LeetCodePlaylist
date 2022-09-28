class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        prod = 1
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
    def similarSolution(self, nums, k):
        start, end, prod, ans = 0, 0, 1, 0
        while end < len(nums):
            prod *= nums[end]
            while end >= start and prod >= k:
                prod /= nums[start]
                start += 1
            ans += end - start + 1
            end += 1
        return ans