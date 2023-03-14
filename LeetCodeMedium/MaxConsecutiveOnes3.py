# https://leetcode.com/problems/max-consecutive-ones-iii/solutions/719833/python3-sliding-window-with-clear-example-explains-why-the-soln-works/?orderBy=most_votes
# In the below implementatin the window doesn't shrink, left pointer doesn't come closer when there is chance to get bigger window size meanwhile right pointer keeps moving right

class Solution:
    def longestOnes(self, nums, k):
        left = right = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

s = Solution()            
s.longestOnes()
       