# approach 1 dynamic programming


def maxSumSubArray(arr):
    max_global = max_here = arr[0]
    for i in range(1, len(arr)):
        max_here = max(arr[i], max_here + arr[i])
        max_global = max(max_here, max_global)
    return max_global


# print(maxSumSubArray([-1,-10,-20,-30,1]))


def maxSumSubArray2(arr):
    max_total = float("-inf")
    total = 0
    for num in arr:
        if num > total + num:
            total = num
        else:
            total = total + num
        max_total = max(max_total, total)
    return max_total


def maxSubArray(nums):
    max_sum = -float("inf")
    curr_sum = 0

    # using Kadane's Algorithm
    for num in nums:
        curr_sum += num

        # updating maximum sum
        if curr_sum > max_sum:
            max_sum = curr_sum

        # if anytime our curr_sum becomes less than 0, we remove the extra baggages.
        # and sets the curr_sum = 0
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


print(maxSumSubArray2([-1001, 60, 7, -50, 60]))
