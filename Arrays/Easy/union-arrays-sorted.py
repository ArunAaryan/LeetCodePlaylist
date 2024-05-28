arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]


# arr1 and arr2 are sorted
def union(arr1, arr2):
    if not len(arr1):
        return arr2
    if not len(arr2):
        return arr1

    first, second = 0, 0
    new_arr = [0]
    while first < len(arr1) and second < len(arr2):
        if arr1[first] <= arr2[second]:
            if new_arr[-1] != arr1[first]:
                new_arr.append(arr1[first])
            first += 1
        else:
            if new_arr[-1] != arr2[second]:
                new_arr.append(arr2[second])
            second += 1
    while first < len(arr1):
        new_arr.append(arr1[first])
        first += 1
    while second < len(arr2):
        new_arr.append(arr2[second])
        second += 1
    return new_arr[1:]


result = union(arr1, arr2)
print(result)
