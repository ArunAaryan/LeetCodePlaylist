class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for current in range(n):
            while nums[current] > 0 and nums[current] <= n and nums[nums[current] - 1] != nums[current]:
                print(current, nums[nums[current] - 1], nums[current])
                nums[nums[current] - 1], nums[current] = nums[current], nums[nums[current] - 1]
        for current in range(n):
            if current + 1 != nums[current]:
                return current + 1
        return n + 1;
    
s = Solution()
res = s.firstMissingPositive([3,4,-1,1])
print(res)


                
        
            
        