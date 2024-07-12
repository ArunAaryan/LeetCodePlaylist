def findFloorAndCeil(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            floor = nums[mid]
            ceil = nums[mid]
            return [floor, ceil]

        elif nums[mid] < target:
            floor = nums[mid]
            low = mid + 1
        else:
            ceil = nums[mid]
            high = mid - 1
    return [floor, ceil]


res = findFloorAndCeil([1, 2, 3, 5, 6, 7], 4)
print(res)
