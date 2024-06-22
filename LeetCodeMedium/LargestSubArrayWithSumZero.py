class Solution:
    def findSubArrayLength(self, arr):
        sum_map = {}  # stores the first seem sum's index
        cummulative_sum = 0
        # stores the cummulative sum till now
        max_len = 0
        # max sub array sum
        left = 0
        right = 0
        for i in range(len(arr)):
            cummulative_sum += arr[i]
            # If cumulative sum is 0, it means that the subarray from the start to the current index sums to 0
            if cummulative_sum == 0:
                max_len = i + 1
                right = i

            # If cum_sum has been seen before, there is a zero sum subarray
            if cummulative_sum in sum_map:
                max_len = max(max_len, i - sum_map[cummulative_sum])
                left = sum_map[cummulative_sum] + 1
                right = i + 1
            else:
                sum_map[cummulative_sum] = i
        print(left, right)
        print(arr[left:right])
        return max_len


s = Solution()
res = s.findSubArrayLength([15, -2, 2, -8, 1, 7, 10, 23])
print(res)
