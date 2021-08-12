class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        close_total = nums[0] + nums[1] + nums[2]
        for first in range(len(nums) -2 ):
            second = first + 1
            third = len(nums) - 1
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                if   abs(total - target)< abs(close_total - target):
                    close_total = total
                if total < target:
                    second += 1
                elif total > target:
                    third -= 1
                else:
                    return total
            return close_total 
s = Solution()
res = s.threeSumClosest([-3,-2,-5,3,-4],-1)
print(res)
        