arr = [4, 2, 2, 1, 1]


def find_single_element(arr):
    seen = {}
    for val in arr:
        if val in seen:
            seen.pop(val)
        else:
            seen[val] = 1
    return seen.popitem()[0]


# res = find_single_element(arr)
# print(res)


def find_single_element_xor(arr):
    if len(arr) == 0:
        return
    xor = arr[0]
    for i in range(1, len(arr)):
        xor ^= arr[i]
    return xor


res = find_single_element_xor(arr)
print(res)
