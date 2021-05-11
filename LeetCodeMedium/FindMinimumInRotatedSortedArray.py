#You use while (start <= end) if you are returning the match from inside the loop.

#You use while (start < end) if you want to exit out of the loop first, and then use the result of start or end to return the match.
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid]  > nums[mid + 1]:
                right = mid 
            else:
                left = mid + 1
        return left   
    
s = Solution()
res = s.findMin([1,2,1,3,5,6,4])
print(res)



            

                


        