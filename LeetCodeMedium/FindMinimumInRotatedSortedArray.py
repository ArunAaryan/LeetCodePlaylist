class Solution:
    def findMin(self, nums):
        size  = len(nums)
        left = 0
        right = size - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2 
            if nums[mid] > nums[left]:
                left = mid +1
            else:
                right = mid 
        return nums[left]

s = Solution()
res = s.findMin([4,5,6,7,0,1,2])
print(res)



            

                


        