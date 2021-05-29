class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            #check if mid is greater than mid + 1, if it greater then peak element must be in left, 
            # in the worst case mid coudl be peak, or left element must definitely be lesser or 
            # equal to peak as this is sorted aray.
            if nums[mid]  > nums[mid + 1]:
                right = mid 
            #same applies here, mid+1 could be the peak element or the last element towards right could be peak
            #right element could be equal or greater than middle.
            else:
                left = mid + 1
        return mid
    def findPeakElement1(self, nums):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if (mid-1<0 or nums[mid]>nums[mid-1]) and (mid+1>=len(nums) or nums[mid]>nums[mid+1]):
                return mid
            elif mid-1>=0 and nums[mid]<nums[mid-1]: # the opposite of the above "if" are these two "elif"
                r = mid - 1
            elif mid+1<len(nums) or nums[mid]<nums[mid+1]:
                l = mid + 1
        return l

s = Solution()          
res = s.findPeakElement([1,3,3,5,3,5])
print(res)

