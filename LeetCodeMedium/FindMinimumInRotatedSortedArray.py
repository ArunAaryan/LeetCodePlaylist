#You use while (start <= end) if you are returning the match from inside the loop.

#You use while (start < end) if you want to exit out of the loop first, and then use the result of start or end to return the match.
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid]  >= nums[left]:
                left = mid + 1 
            else:
                right = mid
        return nums[left]
    
s = Solution()
# res = s.findMin([1,2,1,3,5,6,4])
res = s.findMin([3,4,5,1,2])
print(res)



            

                


        
