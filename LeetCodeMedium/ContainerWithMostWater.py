class Solution:
    def maxArea(self, height):
        left = 0 
        max_current = 0 
        while left <= len(height) - 2:
            current =  0
            right = left + 1
            while right < len(height):
                current = max(current, (right - left ) * min(height[left], height[right]))
                right += 1
            left += 1
            max_current = max(current, max_current)
        return max_current

s = Solution()
# res = s.maxArea([1,8,6,2,5,4,8,3,7])
res = s.maxArea([1,1])
# res = s.maxArea([2,1])
print(res)

        
        