from typing import List
class Solution:
    def __init__(self):
        self.counter = 0

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.depthCalls = 0
        currentSum = 0
        index = 0
        self.bruteForce(nums, currentSum, index, S)
        print('depth calls bruteforece',self.depthCalls)
        return self.counter

    def bruteForce(self, nums, currentSum, index, S):
        self.depthCalls += 1
        if index == len(nums):
            if currentSum == S:
                self.counter += 1
        else:
            self.bruteForce(nums, currentSum + nums[index],index + 1, S)
            self.bruteForce(nums, currentSum  -nums[index], index + 1, S)

    def findTargetSumWaysUsingDp(self, nums, S):
        self.depthCalls = 0
        self.memo = {}
        res = self.dp(nums, 0, S, len(nums)-1) # nums, currentSum, target(S), index
        print('depth calls', self.depthCalls)
        return res
    
    def dp(self, nums, currentSum, S, index):
        self.depthCalls += 1
        if (currentSum, index) in self.memo:
            return self.memo[(currentSum, index)]

        if index < 0 and S == currentSum:
            return 1
        
        if index < 0:
            return 0

        positive = self.dp(nums, currentSum + nums[index], S, index - 1)
        negative = self.dp(nums, currentSum - nums[index], S, index - 1)

        self.memo[(currentSum, index)] = positive + negative
        return self.memo[(currentSum, index)]



                
            
s = Solution()
res = s.findTargetSumWaysUsingDp([35,25,24,23,2,47,39,22,3,7,11,26,6,30,5,34,10,43,41,28],49)
res = s.findTargetSumWays([35,25,24,23,2,47,39,22,3,7,11,26,6,30,5,34,10,43,41,28],49)
print(res)