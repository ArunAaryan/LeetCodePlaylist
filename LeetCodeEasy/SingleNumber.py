#Day 2
# print(2 ^ 2 ^ 3) # n ^ n would result in zero . so remaning element is the answer.
class Solution:
    def singleNumber(self, nums) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
        