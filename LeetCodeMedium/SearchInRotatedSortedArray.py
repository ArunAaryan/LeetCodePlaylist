#https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/273622/Javascript-Simple-O(log-N)-Binary-Search-Solution
# *** When you divide the rotated array into two halves, using mid index, at least one of subarray should remain sorted ALWAYS.

# [3, 4, 5, 6, 7, 1, 2]
# -> [3, 4, 5] [ 6, 7, 1, 2]
# the left side remains sorted

# [6, 7, 1, 2, 3, 4, 5]
# -> [6, 7, 1] [2, 3, 4, 5]
# the right side remains sorted

# [1, 2, 3, 4, 5, 6, 7]
# -> [1, 2, 3] [4, 5, 6, 7]
# Both sides remain sorted.

# If you know one side is sorted, the rest of logic becomes very simple.
# If one side is sorted, check if the target is in the boundary, otherwise it's on the other side.
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
     
        return -1


        
s = Solution()
res = s.search([4,5,6,7,0,1,2], 0)
print(res)