#Day 1
class Solution:
    def missingNumber(self, nums) -> int:
        val = len(nums)
        for i in range(len(nums)):
            val ^= nums[i]
            val ^= i
        return val
       
    def missingNumberHashSet(self, nums) -> int:
        n = len(nums)
        allNumbers = set(nums)
        for i in range(n + 1):
            if i not in allNumbers:
                return i
    
    def missingNumberNFormula(self, nums) -> int:
        n = len(nums)
        sumOfNums = (n * (n + 1)/2) # Sum of whole numbers
        actualSum = sum(nums)
        return int(actualSum - sumOfNums)

        

