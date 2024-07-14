def findFirstOccurence(nums, target):
    low, high = 0, len(nums) - 1
    firstOccurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            firstOccurrence = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return firstOccurrence


def findLastOccurence(nums, target):
    low, high = 0, len(nums) - 1
    lastOccurrence = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            lastOccurrence = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return lastOccurrence


def findPositions(nums, target):
    firstOccurrence = findFirstOccurence(nums, 8)
    if firstOccurrence == -1:
        return [0, 0]
    else:
        lastOccurrence = findLastOccurence(nums, 8)
        return [firstOccurrence, lastOccurrence]


nums = [1, 8, 8, 8, 8, 9, 10]
target = 8


res = findPositions(nums, 8)
print(res)
