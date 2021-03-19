from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totSum = sum(nums)
        if (totSum % k) != 0: # This means that the subsets are not equally divisible
            return False
        if len(nums) < k: # This means that aren't enough elements to partition into k subsets
            return False
        subsetSum = totSum / k
        print(subsetSum)
        return self.backtrack(nums, 0, 0, k, subsetSum, [False] * len(nums))

    def backtrack(self,nums, start, curSum, k,  targetSum, used):
        if k == 1: return True # This means all the remaining subsets are being found then the only possibility \
        # is that the next subset is also found because of the case (totSum %k )!= 0. 
        if curSum > targetSum: return False # if adding the new element in previous recursion leads to curSum greater than required then it 
        #is false
        if curSum == targetSum: # if currentPair with curSum == targetSum is found find the remaining k-1 subsets
            return self.backtrack(nums, 0, 0, k-1, targetSum, used)
        
        for i in range(start, len(nums)):
            if used[i]: continue
            used[i] = True
            if self.backtrack(nums, i + 1, curSum + nums[i],k, targetSum, used): # use the next element and find the next subset.
                return True 
            used[i] = False #If the above statement fails remove the element and use the next element.
        # print('came here')
        return False
        


s = Solution()
res = s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6],3)
print(res)
    