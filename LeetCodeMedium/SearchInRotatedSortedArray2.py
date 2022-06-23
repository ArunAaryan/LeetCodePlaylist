class Solution:
    class Solution:
    # the solution is same as rotate sorted array 1

        def search(self, nums: List[int], target: int) -> bool:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                # skip duplicates using this below technique.
                # skips duplicates from current left position // skips current left values if same vice versa for right
                while (left < mid and nums[left] == nums[mid]):
                    left += 1
                while (right > mid and nums[right] == nums[mid]):
                    right -= 1
                if nums[left] <= nums[mid]: # nums[left] '<=' means include mid in left search space .
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                        
            return False

    def search(self, nums, target ):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] == nums[mid]:
                left += 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
     
        return False
s = Solution()
# res = s.search([2,5,6,0,0,1,2],0)
# res = s.search([1,1,1,0,1], 0)
res = s.search([1], 1)
print(res)


            
        
        