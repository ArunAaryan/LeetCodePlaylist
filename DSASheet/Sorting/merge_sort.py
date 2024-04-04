# https://takeuforward.org/data-structure/merge-sort-algorithm/
arr = [90,20, 43, 10, 2, 7, 47, 42, 36]

#  mergeSort method to divide elements upto 1
# if the length is already 1 return
# else mid = low + high // 2,  

def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid: # still less than mid means elements left on the left side
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    # copy the elements in the order to arr
    for i in range(low, high + 1): # include the element at the last also.
        arr[i] = temp[i - low] # because temp is a subset of arr and has less
        # elements 
    return

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)
mergeSort(arr, 0, len(arr) - 1)
print(arr)