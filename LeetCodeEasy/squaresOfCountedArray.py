from collections import deque


def sortedSquares(nums):
    dq = deque()
    lo, high = 0, len(nums) - 1
    while lo <= high:
        left, right = abs(nums[lo]) , abs(nums[high])
        if left > right:
            dq.appendleft(left * left)
            lo += 1
        else:
            dq.appendleft(right * right)
            high -= 1
    return list(dq)

s = sortedSquares([-17, -11, 15, 16])
print(s)