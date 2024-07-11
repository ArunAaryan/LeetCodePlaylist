def findLowerBound(nums, target):
    if not nums:
        return -1
    if len(nums) == 1:
        if nums[0] <= target:
            return nums[0]
        return -1
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid

    return nums[low]


res = findLowerBound([1, 3, 3, 3, 5, 7, 9], 3)
print(res)
