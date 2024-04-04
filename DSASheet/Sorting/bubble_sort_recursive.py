arr = [90,20, 43, 10, 2, 7, 47, 42, 36]


def bubble_sort(arr, n):
    if n == 1:
        return
    swapped = 0
    for j in range(n - 1):
        if arr[j + 1] < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = 1
    # if the arr is already sorted at this range from (0, n) then no swap will occur.
    # hence it will reduce the time complexity, so in the worst case
    # it will be O(n)
    if swapped:
        bubble_sort(arr, n - 1)
    return 

bubble_sort(arr, len(arr) - 1)
print(arr)
