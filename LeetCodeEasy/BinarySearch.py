#day 6
arr = [1,2, 3, 4, 5,6, 7, 8, 9, 10]

low = 0
high = len(arr) - 1
x = 4
def findUsingBinarySearch(arr, x, low, high):
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid - 1 
        else:
            low = mid + 1
    return -1
print('found element at ',findUsingBinarySearch(arr, x, low, high))