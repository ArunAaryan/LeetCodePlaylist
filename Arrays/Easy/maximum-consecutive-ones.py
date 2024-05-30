arr = [1, 1, 1, 0, 1, 0, 1, 0]


def findMaxCount(arr):
    max_count = count = 1
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count


res = findMaxCount(arr)
print(res)
