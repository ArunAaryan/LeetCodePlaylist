class Solution:
    def twoSum(self, nums, target):
        targetMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in targetMap:
                return [i, targetMap[diff]]
            targetMap[nums[i]] = i
        return []
            
        
                    
        