class Solution:
    def runningSum(self, nums):
        sum_till_now = 0
        output = []
        for i in nums:
            sum_till_now += i
            output.append(sum_till_now)
        return output

s = Solution()
ans = s.runningSum([1, 2, 3, 4])
print(ans)
