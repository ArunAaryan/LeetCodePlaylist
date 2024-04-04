arr = [90,20, 43, 10, 2, 7, 47, 42, 36]

def insertion_sort(arr, i, n):
    if n == i:
        return
    for j in range(i, 0, -1):
        if arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
    insertion_sort(arr, i + 1, n) 
    return

insertion_sort(arr, 0, len(arr))
print(arr)