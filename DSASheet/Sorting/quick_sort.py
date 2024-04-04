# https://takeuforward.org/data-structure/quick-sort-algorithm/
arr = [90,20, 43, 10, 2, 7, 47, 42, 36]

def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j 

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
quick_sort(arr, 0, len(arr) - 1)
print(arr)