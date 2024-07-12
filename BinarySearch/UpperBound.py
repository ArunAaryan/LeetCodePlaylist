def find_upper_bound(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return nums[low]


res = find_upper_bound([1, 2, 3, 5, 6], 4)
print(res)
