arr = [24,69,100,99,79,78,67,36,26,19]

low, high = 0, len(arr) - 1

def peakIndexMountainArray(arr, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            high = mid - 1
    return mid, low
     
print(peakIndexMountainArray(arr, 0, len(arr)-1))
