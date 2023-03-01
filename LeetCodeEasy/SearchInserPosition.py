class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
s = Solution()
ans = s.searchInsert([1, 3, 5, 6], 7)
print(ans)

                

# x = 1 
# y = 10
# print( (y - x) // 2 + x)
# print((x + y) // 2)