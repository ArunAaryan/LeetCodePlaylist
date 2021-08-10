class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for fixed in range(len(nums) - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            second = fixed + 1
            third = len(nums) - 1
            while second < third:
                total = nums[fixed] + nums[second] + nums[third]
                if total < 0:
                    second += 1
                elif total > 0:
                    third -= 1
                else:
                    res.append([nums[fixed], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    second += 1
                    third -= 1
        return res
                            

s = Solution()
res = s.threeSum([-1,0,1,2,-1,-4])
print(res) 
        