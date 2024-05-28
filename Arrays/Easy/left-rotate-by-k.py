arr = [1, 2, 3, 4, 5, 6]
# arr= [6, 5, 4, 3, 2, 1]
# arr = [3, 4, 5, 6, 1, 2]
# arr = [3, 4, 5, 6, 1, 2]
k = 2
def _rotate(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[i] = temp 

def rotate(arr, k):
    r = k % len(arr)
    if r == len(arr):
        return arr 
    for _ in range(r):
        _rotate(arr)
    


# rotate(arr, k)
# print(arr)
def rotateReverse_(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    
def rotateReverse(arr, k):
    k %= len(arr)
    if len(arr) == k:
        return arr 
    rotateReverse_(arr, 0, len(arr) - 1)
    rotateReverse_(arr, 0,  k - 1)
    rotateReverse_(arr, k ,  len(arr) - 1)
rotateReverse(arr, k)
print(arr)