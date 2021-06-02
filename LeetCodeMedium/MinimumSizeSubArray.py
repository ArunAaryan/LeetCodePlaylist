class Solution:
    def minSubArrayLen(self, target, nums) :
        left = 0
        right = 0
        total = 0
        ml = len(nums) + 1 
        while right < len(nums) and left <= right:
            total += nums[right]
            while (total >= target):
                ml = min(right - left + 1, ml)
                total -= nums[left]
                left += 1
            right += 1
        return ml if ml != len(nums) + 1 else 0 
s = Solution()
res = s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3,7])
print(res)