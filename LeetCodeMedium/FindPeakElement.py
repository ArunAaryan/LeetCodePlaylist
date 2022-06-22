class Solution:
    def findPeakElement(self, nums):
        #corner cases
        if len(nums) == 1:
            return 0
        n = len(nums) - 1
        if nums[0] > nums[1]: # based on constraint nums[i] != nums[i + 1] and we can return any of the peek
            return 0
            # so if this is one of the peek we can consider it
        if nums[n] > nums[n - 1]:
            return n
        start, end = 1, n - 1
        
        while start <= end: # = sign means handling mid inside the loop
            mid = (start + end) // 2
            if (nums[mid] > nums[mid - 1]) and (nums[mid] > nums[mid + 1]):
                return  mid 
            elif nums[mid] < nums[mid - 1]:
                end = mid - 1
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1

    
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

