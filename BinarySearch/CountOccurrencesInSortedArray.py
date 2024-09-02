def findCountOccurrences(arr, target):
    left_index = findLeftMostOccurrence(arr, target)
    right_index = findRightMostOccurrence(arr, target)
    return right_index - left_index + 1


def findLeftMostOccurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
            #  we found the element in range; now we try find the lef
            # most with this condition right = mid - 1
        elif mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def findRightMostOccurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
            #  we found the element in range; now we try find the right
            # most with this condition left = mid + 1
        elif mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


arr = [1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 7, 9]
result = findCountOccurrences(arr, 3)
print(result)
