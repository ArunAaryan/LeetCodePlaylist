arr = [90,20, 43, 10, 2, 7, 47, 42, 36]
def is_sorted(arr):
    if len(arr) == 1:
        return True
    small = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < small:
            return False
    return True

print(is_sorted(arr))
